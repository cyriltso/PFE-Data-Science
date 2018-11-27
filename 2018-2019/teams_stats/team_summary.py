from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

site= "https://fr.whoscored.com/Regions/250/Tournaments/12/Seasons/7352/Stages/16704/TeamStatistics/Europe-UEFA-Champions-League-2018-2019"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
print(soup)