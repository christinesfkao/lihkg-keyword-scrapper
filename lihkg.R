install.packages("LIHKGr")
install.packages("rio")
library(LIHKGr)
library(rio)

## Creating a Firefox instance with a random port.
keyword <- commandArgs(trailingOnly = TRUE)
threadids <- as.vector(read.csv(keyword +"_links_id.txt"))
print("The keyword you selected is \"" + keyword + "\", with " +length(threadids[[1]]) + "threads.")
lihkg <- create_lihkg(browser = "firefox", port = sample(10000:60000, 1), verbose = FALSE)

print("Preparing for scrapping at " + date())
lihkg$scrape(threadids$V1)
print(head(lihkg$bag))

print("Exporting scrapped contents...")
rio::export(lihkg$bag, keyword + "_contents.xlsx")

lihkg$finalize()
print("End of program at " + data())

