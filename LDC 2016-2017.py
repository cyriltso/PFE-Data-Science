import os #allow to do a break at the end of the script
import csv #export to a csv file
import requests #used to load the page and to store the contents inside of a variable
from bs4 import BeautifulSoup

write_to_file_path = "LDC 2016-2017.csv";
output_file = open(write_to_file_path, "w+");
writer = csv.writer(output_file)

requete = requests.get("https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League") #requests.get allows to do a HTTP/HTTPS request
page = requete.content #the method content allows to get the content of the page
soup = BeautifulSoup(page, "html.parser") #the page is parsed with BeautifulSoup

#print(soup) #used to scrap the whole page

#print(soup.find_all('p')) #used to find all the paragraphs
#print(soup.find_all('h3')) #used to scrap all the subtitles

#print(soup.findAll('div',attrs={"class":"wikitable"}))

table = soup.find('table', attrs={'class':'multicol'}) #the whole table in which are stored the data on the website, multicol is the class corresponding to the ranking of the scorers and the assists

for line in table.findAll('tr'): #parsing an entire row
    for l in line.findAll('td'): #parsing each row
        if l.find('sup'):
           l.find('sup').extract()
        print(l.getText(),'-'),
    print



