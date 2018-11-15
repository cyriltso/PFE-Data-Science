### Librairies ###

import csv
from bs4 import BeautifulSoup
import urllib.request

### URL selection, reading and parsing ###

url = "https://fr.wikipedia.org/wiki/Ligue_des_champions_de_l'UEFA"
parser = urllib.request.urlopen(url).read()
soup = BeautifulSoup(parser, 'lxml')

### CSV file in which the data will be written ###

csv_file = open('Most Appearances : Coaches.csv', 'w', newline='', encoding="UTF-8")
writer = csv.writer(csv_file)

### Data Selection ###

tables = soup.findAll('table', {'class':'wikitable'}) #selecting the whole table
#print(tables) #checking if the tables contain the one we want

fst_table = tables[0] #first table
#print(fst_table)

snd_table = tables[1] #second table
#print(snd_table)

thd_table = tables[2] #third table
#print(thd_table)

fth_table = tables[3] #fourth table
#print(fth_table)

ffth_table = tables[4] #fifth table
#print(ffth_table)

six_table = tables[5] #sixtb table
#print(six_table)

titles = six_table.findAll('th') #selecting the titles of the table
#print(titles)
#print(titles[2].get_text())

lines = six_table.findAll('tr') #selecting the lines of the table
#print(lines)
#print(lines[1].get_text())

### Parsing, Selection and Storing of the data ###

writer.writerow(('Ranking', 'Name', 'Clubs', 'Matches', 'Trophies'))
for line in lines:
    data = line.findAll('td')
    try:
        if data:
            rank = data[0].get_text()
            name = data[1].get_text()
            club = data[2].get_text()
            match = data[3].get_text()
            trophie = data[4].get_text()
            print(rank, name, club, match, trophie)
            writer.writerow((rank, name, club, match, trophie))
    except:
        pass