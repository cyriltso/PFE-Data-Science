#importing libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#selecting the url
page_selected = 'https://en.wikipedia.org/wiki/2017%E2%80%9318_UEFA_Champions_League'

#calling the website and returning the hyperlink to the variable 'page_selected'
page = urllib.request.urlopen(page_selected)

#parsing the html with BeautifulSoup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

soup_text_extract = soup.text.strip()

print(soup) #used to print the content of the web page
print(soup_text_extract) #used to print the extracted text of this page

#selecting a specific data on the webpage
page_section = soup.find('h1', attrs={'class': 'firstHeading'})
page_section2 = soup.find("div", {"id": "bodyContent"})
page_section3 = soup.find("table", {"class": "infobox vcalendar"})

#scrap elements that are from the same class
for elements in soup.find_all("table", {"class": "wikitable"}):
    print(elements.text.strip())

#extracting the text in this tag section
text = page_section.text.strip() #strip() allows extract the text inside of the tags
text2 = page_section2.text.strip()
text3 = page_section3.text.strip()

print(page_section)
print(text2)
print(text3)

#open a csv file in which data are written inside
with open('LDC 2017-2018 data.csv', 'a', encoding="UTF-8") as csv_file:
    writer = csv.writer(csv_file)
    w = writer.writerow([text3, datetime.now()])


