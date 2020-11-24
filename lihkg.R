#install.packages("LIHKGr")
#install.packages("rio")
library(LIHKGr)
library(rio)

## Creating a Firefox instance with a random port.
keyword <- commandArgs(trailingOnly = TRUE)
filename <- paste(keyword, "links.txt", sep = "")
threadids <- read.table(filename)[[1]]
paste("The keyword you selected is \'", keyword, "\', with ", length(threadids), " threads.", sep = "")
lihkg <- create_lihkg(browser = "firefox", port = sample(10000:60000, 1), verbose = FALSE)

paste("Preparing for scrapping at" , date())
lihkg$scrape(threadids)
print(head(lihkg$bag))

print("Exporting scrapped contents...")
rio::export(lihkg$bag, keyword + "_contents.xlsx")

lihkg$finalize()
print("End of program at" , date())

