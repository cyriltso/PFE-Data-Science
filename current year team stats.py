import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

page_selected = 'https://fr.uefa.com/uefachampionsleague/season=2019/statistics/'

page = urllib.request.urlopen(page_selected)
soup = BeautifulSoup(page, 'html.parser')

soup_text_extract = soup.text.strip()

#print(soup)
#print(soup_text_extract)

stats = soup.find('div', attrs={'class': 'container-fluid'})
stats_extract = stats.text.strip()

print(stats_extract)

with open('current year stats', 'a', encoding="UTF-8", newline='') as csv_file:
    writer = csv.writer(csv_file)
    w = writer.writerow([stats_extract, datetime.now()])

