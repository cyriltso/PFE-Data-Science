import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

page_selected = 'https://www.lequipe.fr/Football/HIST_C1.html'

page = urllib.request.urlopen(page_selected)
soup = BeautifulSoup(page, 'html.parser')

soup_text_extract = soup.text.strip()

#print(soup)
#print(soup_text_extract)

winners_list = soup.find('div', attrs={'id': 'Base'})
winners_text = winners_list.text.strip()

print(winners_text)

with open('CL Prize Winner.csv', 'a', encoding="UTF-8", newline='') as csv_file:
    writer = csv.writer(csv_file)
    w = writer.writerow([winners_text, datetime.now()])
