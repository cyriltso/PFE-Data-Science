### Librairies ###

import csv
from bs4 import BeautifulSoup
import urllib.request

### URL selection, reading and parsing ###

url = 'https://en.wikipedia.org/wiki/UEFA_Champions_League'
parser = urllib.request.urlopen(url).read()
soup = BeautifulSoup(parser, 'lxml')

### CSV file in which the data will be written ###

csv_file = open('perf_nation.csv', 'w', newline='', encoding="UTF-8")
writer = csv.writer(csv_file)

### Data Selection ###

tables = soup.findAll("table", {"class":"wikitable plainrowheaders sortable"}) ## the problem here is that this class selects two tables that got the same class tag ##
fst_table = tables[0] #selecting the first table
scd_table = tables[1] #selecting the second table, the table that we will extract the data here

#print(fst_table)
#print(scd_table)

header = scd_table.findAll('th') #selecting all the titles of the table at the top
#print(header)

lines = scd_table.findAll('tr')
#print(lines)
#print(lines[1].get_text()) #test to check if the content of the second line of the table interests us or not

cnt_check = scd_table.findAll('td')
#print(cnt_check)

### Parsing, Collecting and Storing the data into the CSV file ###

writer.writerow(('Nation', 'Titles', 'Runners-up', 'Total'))

for line in lines:
    countries = line.findAll('th')
    numbers = line.findAll('td')
    try:
        if countries and numbers:
            country = countries[0].get_text()
            title = numbers[0].get_text()
            run_up = numbers[1].get_text()
            total = numbers[2].get_text()
            print(country, title, run_up, total)
            writer.writerow((country, title, run_up, total))
    except:
        pass