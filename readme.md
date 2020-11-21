# README.md
This is the README file for```lihkg-keyword-scrapper```by [@christinesfkao](https://github.com/christinesfkao).

Adapted from: Ho, J.C. & Or, N.H.K. (2020). [LIHKGr](https://github.com/justinchuntingho/LIHKGr): An application for scraping LIHKG.

Last updated: Nov 2020
## Directory
```
lihkg-scrapper.py	
lihkg.R	 
README.md
```

## Synopsis
```
python3 lihkg-scrapper.py [keyword]
RScript lihkg.R [keyword]
```
LIHKG, aka 連登, is the most popular internet forum in Hong Kong in 2019.

```lihkg-scrapper.py```can scrape the url of threads whose title include specific keywords; then dump them into [LIHKGr](https://github.com/justinchuntingho/LIHKGr) with```lihkg.R```to download contents of the thread.

## Environment  
Feel free to set up according to your preferences. The following is what I used.

- MacOS Catalina 10.15.7 (x86_64-apple-darwin17.0)
- Firefox Browser 83.0 (64-bit)
- Python 3.9.0
- R version 4.0.3

## Before running 
0. Decide on the keyword(s) you're going to search for
	- for```python3 lihkg-scrapper.py [keyword]```, the keyword would be read in as```sys.argv[1]```in my module and  *put on the search bar* during the automation process
	- for```Rscript lihkg.R [keyword]```, read in with ```commandArgs(trailingOnly = true)```
1. Check your environment settings from [Selenium documents on Python](https://selenium-python.readthedocs.io/installation.html)
	- install Python bindings for selenium:```pip3 install selenium```
	- download (and install) the web broswer driver that you have chosen
	- no need for JAVA server for this scrapper

2. Put the downloaded [geckodriver for Firefox](https://github.com/mozilla/geckodriver/releases) (or the driver for your preferred browser) under your desired directory 
	- **preferred $PATH setting method**: Special thanks to [@shouko](https://github.com/shouko)'s advice
3. Change the constants in ```lihkg-scrapper.py``` according to your needs: 
	- ```PATH```as your desired directory
	-  Account```USERNAME```and```PASSWORD```for LIHKG (**Preferred: apply for a LIHKG account before scrapping!**)
	-  Or you could choose to input these rather sensitive information manually

## Outputs

- The Python script outputs thread ids into a```.txt```file, one id for each line
	- ```lihkg-scrapper.py``` scrapes the url of threads, but outputs include only the thread ids 
	- e.g. in [https://lihkg.com/thread/#######/page/1](), only ####### is left in the output 
- The R script outputs contents of the threads into a```.xlsx```file
	- the ids saved in the```.txt```file are read in as a vector and thrown into [LIHKGr](https://github.com/justinchuntingho/LIHKGr)
	- ```lihkg.R```download contents of the thread in to an```.xlsx```file.

	
## To-dos
I haven't finished the code on R for logging in yet. Perhaps the entire process can then be done in a single R script. PRs welcome!
