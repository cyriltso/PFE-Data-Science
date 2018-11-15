### Librairies ###

import csv
from bs4 import BeautifulSoup
import urllib.request

### URL selection, reading and parsing ###

url = 'https://en.wikipedia.org/wiki/UEFA_Champions_League'
parser = urllib.request.urlopen(url).read()
soup = BeautifulSoup(parser, 'lxml')

### CSV file in which the data will be written ###

csv_file = open('Alltime_Winners.csv','w',newline='',encoding="UTF-8")
writer = csv.writer(csv_file)

### Data Selection ###

winners = soup.find("table", {"class":"wikitable plainrowheaders sortable"}) #selecting the whole table
lines = winners.findAll('tr') #selecting all the lines of the table
titles = winners.findAll('th') #selecting the titles of the table
contents = winners.findAll('td') #selecting the contents of the table

### Testing the table selection before browsing it to only extract relevant informations from the table ###

#print(titles[5].get_text()) ## used to select the clubs' section in the table as they are classified with "th" tags ##
#print(contents[0].get_text()) ## first element of the contents surrounded by "td" tags ##
#print(lines[1].get_text()) ## text content of the second line of the table ##

### Selection, Extraction and Storing the data on CSV file ###


writer.writerow(('Club', 'Titles', 'Runners-up', 'Winning Seasons', 'Runner-up Seasons'))
for line in lines:
    clubs = line.findAll("th")
    other_elements = line.findAll("td")
    try:
        if clubs and other_elements:
            club = clubs[0].get_text()
            titles = other_elements[0].get_text()
            runners_up = other_elements[1].get_text()
            w_seasons = other_elements[2].get_text()
            r_up_seasons = other_elements[3].get_text()
            print(club, titles, runners_up, w_seasons, r_up_seasons)
            writer.writerow((club, titles, runners_up, w_seasons, r_up_seasons))
    except:
        pass


