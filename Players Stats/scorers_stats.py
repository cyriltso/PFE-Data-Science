from selenium import webdriver
import pandas as pd
import os

chro_path = '/Users/cyriltso/Documents/UCL Statistics/chromedriver'

browser = webdriver.Chrome(os.path.join(os.getcwd(), chro_path))

path = "/Users/cyriltso/Documents/UCL Statistics/Players Stats/Best Scorers"

url = 'http://www.espn.com/soccer/stats/_/league/UEFA.CHAMPIONS/season/2016'
browser.get(url)

table = browser.find_element_by_xpath('//*[@id="fittPageContainer"]/div[3]/div[1]/div[1]/article/div/article/div/'
                    'section/div/div[1]/section/section/table/tbody/tr/td/div/div/div[2]/table/tbody/tr/td/table')

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
        if content[0].isdigit():
            content.insert(0, ' ')
            content.insert(2, ' ')
        else:
            content.insert(0, ' ')
            content.insert(1, ' ')
            content[2] = ' '
    if len(content) == 6:
        if content[0].isdigit():
                content.insert(0, ' ')
                content.insert(2, ' ')
                content.insert(6, ' ')
        else:
                content.insert(0, ' ')
                content.insert(1, ' ')
                content.insert(2, ' ')
    if len(content) == 5:
        content.insert(0, ' ')
        content.insert(1, ' ')
        content.insert(2, ' ')
        content.insert(6, ' ')
    if len(content) == 4:
        content.insert(0, ' ')
        content.insert(1, ' ')
        content.insert(2, ' ')
        content.insert(4, ' ')
        content.insert(6, ' ')

print(players_specs)

# 0, 1, 2 --> RANK
# 3, 4 --> NAME
# 5, 6 --> TEAM
# 7 --> GAMES PLAYED
# 8 --> GOALS SCORED

db = pd.DataFrame({
    'YEAR': season_year[2],
    'CATEGORIES 1': 'Scorers',
    'RANK_S': [i[1] for i in players_specs],
    'NAME_S': [i[3] + ' ' + i[4] for i in players_specs],
    'TEAM_S': [i[5] + ' ' + i[6] for i in players_specs],
    'P_S': [i[7] for i in players_specs],
    'G': [i[8] for i in players_specs]
})

db = db[[
    'YEAR', 'CATEGORIES 1', 'RANK_S', 'NAME_S', 'TEAM_S', 'P_S', 'G'
]]

print(db)

db.to_csv(os.path.join(path, r'2016-2017 UCL Best Scorers stats.csv'), index = False)