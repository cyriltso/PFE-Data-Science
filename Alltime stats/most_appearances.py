### Librairies ###

import csv
from bs4 import BeautifulSoup
import urllib.request

### URL selection, reading and parsing ###

url = 'https://en.wikipedia.org/wiki/UEFA_Champions_League'
parser = urllib.request.urlopen(url).read()
soup = BeautifulSoup(parser, 'lxml')

### CSV file in which the data will be written ###

csv_file = open('Most Appearances.csv', 'w', newline='', encoding="UTF-8")
writer = csv.writer(csv_file)

### Data Selection ###

tables = soup.findAll('table',{'class':'wikitable sortable'}) #selecting the whole table
#print(tables)

fst_table = tables[0] #selecting the first table, which is useless for us in this data acquisition
#print(fst_table)

snd_table = tables[1] #the table that contains the data we want
#print(snd_table)

lines = snd_table.findAll('tr') #selecting every lines all of the table
#print(line_content)

cnt_check = snd_table.findAll('td') #checking if all the contents inside of the "td" tags are the ones wanted by us
#print(cnt_check)

### Parsing, Collecting, Extracting and Storing the Data into the CSV file ###

writer.writerow(('Ranking', 'Player', 'Nation', 'Appearances', 'Years', 'Clubs')) #creating the title of each column of the data that are going to be stored
for line in lines: #as the table is considered as a list of elements, we can parse it like a list to retrieve each single element
    line_content = line.findAll('td') #we want to select each content of each line of the table one by one
    try: #creating an exception in order to avoid the outrange of the parsing (as we don't really know the maximum value)
        if line_content: #checking if the selecting content always exists
            ranking = line_content[0].get_text() #selecting the first element of the 'td' tags inside of the line and extracting the text
            player = line_content[1].get_text()
            nation = line_content[2].get_text()
            app = line_content[3].get_text()
            years = line_content[4].get_text()
            clubs = line_content[5].get_text()
            print(ranking, player, nation, app, years, clubs) #printing the results to check if it worked
            writer.writerow((ranking, player, nation, app, years, clubs)) #writing the data in the CSV file
    except:
        pass #avoid the error message when we have exceeded the range of the table


