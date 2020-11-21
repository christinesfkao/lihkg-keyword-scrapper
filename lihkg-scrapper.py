from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
import re
import sys

# constants: set before running
# PAUSE = 1.5
# PATH = "directory"
# USERNAME = "username"
# PASSWORD = "password"

print("================ Starting browser... ================")
driver = webdriver.Firefox(executable_path= PATH + "/geckodriver")
driver.get("https://lihkg.com/")
driver.maximize_window()
time.sleep(PAUSE)
driver.find_element_by_class_name("i-menu").click()
driver.find_element_by_class_name("i-account").click()
print("=================== Logging in... ===================")
driver.find_element_by_name("email").send_keys(USERNAME)
driver.find_element_by_name("password").send_keys(PASSWORD) 

# automation will pause for manually dealing with recaptcha
print("========== Waiting for manual recaptcha... ==========")
wait = WebDriverWait(driver, 120, poll_frequency=10, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, ElementClickInterceptedException, TimeoutException])
wait.until(EC.invisibility_of_element((By.CLASS_NAME, "_34dVbr5A8khk2N65H9Nl-j")))

print("============= Searching for \"" + sys.argv[1] + "\"... =============")
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "i-menu"))).click()
search = driver.find_element_by_class_name("_1T-sxyP9sVSHKzn4lJ6SVL")
search.send_keys(sys.argv[1])
search.submit()

last_height = driver.execute_script("return leftPanel.scrollHeight;")

while True:
    # Scroll webpage, the "1000" allows for a more "aggressive" scroll
    driver.execute_script("leftPanel.scrollTo(0, 1000+leftPanel.scrollHeight);")
    # Wait to load page
    time.sleep(PAUSE)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return leftPanel.scrollHeight;")
    if (new_height == last_height):
        break
    last_height = new_height
    print("================ Scrolling to the end ================")

print("============== Creating list of threads ==============")
threads = driver.find_elements_by_class_name("_2A_7bGY9QAXcGu1neEYDJB")
links = list()
for thread in threads:
	temp = re.split("/" ,thread.get_attribute("href"))[4] # leave thread ID only
	links.append(temp)

print("================= Writing output file =================")
with open(PATH + sys.argv[1] + "_links_id.txt", 'w') as f:
    f.write("\n".join(links))

driver.quit()
print("=================== End of program ===================")