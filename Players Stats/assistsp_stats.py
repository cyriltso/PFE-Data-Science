from selenium import webdriver
import pandas as pd
import os

chro_path = '/Users/cyriltso/Documents/UCL Statistics/chromedriver'

browser = webdriver.Chrome(os.path.join(os.getcwd(), chro_path))

path = "/Users/cyriltso/Documents/UCL Statistics/Players Stats/Best assists players"

url = 'http://www.espn.com/soccer/stats/_/league/UEFA.CHAMPIONS/season/2016'
browser.get(url)

table = browser.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div[1]/div[1]/article/div/article/div/section/'
                                      'div/div[2]/section/section/table')

table_element = table.text.split('\n')

print(table_element)

season = browser.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div[1]/div[1]/article/div/article/div/div[3]/select[1]')
season_year = season.text.split('\n')
print(season_year)

players_specs = []

for line_rank, lines in enumerate(table_element):
    if line_rank == 0:
        pass
    else:
        players_specs.append(lines.split(' '))

print(players_specs)

for content in players_specs:
    if len(content) == 7:
        pass
    if len(content) == 6:
        if content[0].isdigit():
            content.insert(4, ' ')
        else:
            content.insert(0, ' ')
    if len(content) == 5:
        if content[0].isdigit():
            content.insert(2, ' ')
            content.insert(4, ' ')
        elif content[2] in ('Juventus', 'Napoli', 'Arsenal', 'Barcelona', 'Benfica', 'Rostov', 'Besiktas'):
            content.insert(0, ' ')
            content.insert(4, ' ')
        else:
            content.insert(0, ' ')
            content.insert(2, ' ')
    if len(content) == 4:
        content.insert(0, ' ')
        content.insert(2, ' ')
        content.insert(4, ' ')

print(players_specs)

db = pd.DataFrame({
    'YEAR': season_year[2],
    'CATEGORIES 2': 'Assists',
    'RANK_A': [i[0] for i in players_specs],
    'NAME_A': [i[1] + ' ' + i[2] for i in players_specs],
    'TEAM_A': [i[3] + ' ' + i[4] for i in players_specs],
    'P_A': [i[5] for i in players_specs],
    'A': [i[6] for i in players_specs]
})

db = db[[
    'YEAR', 'CATEGORIES 2', 'RANK_A', 'NAME_A', 'TEAM_A', 'P_A', 'A'
]]

print(db)

db.to_csv(os.path.join(path, r'2016-2017 UCL Best Assists players stats.csv'), index = False)
