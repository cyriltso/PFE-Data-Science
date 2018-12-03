### Librairies ###

from bs4 import BeautifulSoup
import csv
import urllib.request

### URL selection, reading and parsing ###

url = 'https://en.wikipedia.org/wiki/UEFA_Champions_League'
parser = urllib.request.urlopen(url).read()
soup = BeautifulSoup(parser, 'lxml')

### CSV file in which the data will be written ###

csv_file = open('Alltime_Scorers.csv','w',newline='',encoding="UTF-8")
writer = csv.writer(csv_file)

### Data Selection ###

scorers = soup.find("table",{"class":"wikitable sortable"}) #Selecting the related data
lines = scorers.findAll("tr") #Selecting all the table's lines
categories = scorers.findAll("th") #Selecting all the titles of this table
contents = scorers.findAll("td") #Selecting all the lines' contents of the table

#print(contents[78].get_text())
#print(len(contents))

### Selection, extraction and storage of the data on csv ###

writer.writerow(('Ranking', 'Player', 'Country', 'Goals', 'Apps', 'Ratio', 'Years', 'Clubs'))
for element in lines:
    case_content = element.findAll("td")
    try:
        if case_content:
            ranking = case_content[0].get_text()
            player = case_content[1].get_text()
            country = case_content[2].get_text()
            goals = case_content[3].get_text()
            apps = case_content[4].get_text()
            ratio = case_content[5].get_text()
            years = case_content[6].get_text()
            clubs = case_content[7].get_text()
            print(ranking,player,country,goals,apps,ratio,years,clubs)
            writer.writerow((ranking,player,country,goals,apps,ratio,years,clubs))
    except:
        pass
"""
print(contents[0].get_text(), contents[1].get_text(),contents[2].get_text(),contents[3].get_text(), contents[4].get_text(),
                 contents[5].get_text(), contents[6].get_text(), contents[7].get_text())
print(contents[8].get_text(), contents[9].get_text(),contents[10].get_text(),contents[11].get_text(), contents[12].get_text(),
                 contents[13].get_text(), contents[14].get_text(), contents[15].get_text())

writer.writerow(('Ranking', 'Player', 'Country', 'Goals', 'Apps', 'Ratio', 'Years', 'Clubs'))
writer.writerow((contents[0].get_text(), contents[1].get_text(),contents[2].get_text(),contents[3].get_text(), contents[4].get_text(),
                 contents[5].get_text(), contents[6].get_text(), contents[7].get_text()))
writer.writerow((contents[8].get_text(), contents[9].get_text(),contents[10].get_text(),contents[11].get_text(), contents[12].get_text(),
                 contents[13].get_text(), contents[14].get_text(), contents[15].get_text()))
"""

### TEST - Text Extraction of the categories ###
"""
i = 0

for line in categories:
    try:
        categories_text = categories[i].get_text()
        print(categories_text)
        i = i + 1
    except:
        pass

    writer.writerow(line)
"""
### TEST - Text Extraction of the contents ###
"""
j = 0

for row in contents:
    try:
        contents_text = contents[j].get_text()
        print(contents_text)
        j = j + 1
    except:
        pass

    writer.writerow(row)
"""

"""
for line in contents:
    global_stats = line.findAll("td")
    if global_stats:
        ranking = global_stats[0].get_text()
        player = global_stats[1].get_text()
        country = global_stats[2].get_text()
        goals = global_stats[3].get_text()
        apps = global_stats[4].get_text()
        ratio = global_stats[5].get_text()
        years = global_stats[6].get_text()
        clubs = global_stats[7].get_text()
        print(ranking)
"""