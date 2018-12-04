from selenium import webdriver
import pandas as pd
import os

chro_path = '/Users/cyriltso/Documents/UCL Statistics/chromedriver'

browser = webdriver.Chrome(os.path.join(os.getcwd(), chro_path))

path = "/Users/cyriltso/Documents/UCL Statistics/Teams Database/Group Stage"

url = 'http://www.espn.com/soccer/standings/_/league/uefa.champions/season/2016'
browser.get(url)

table = browser.find_element_by_xpath('//*[@id="main-container"]/div/section/div[1]/div/div[2]/table')

table_element = table.text.split('\n')

print(table_element)

season = browser.find_element_by_xpath('//*[@id="main-container"]/div/section/div[1]/div/div[1]/div[2]/button')
season_year = season.text.split('\n')
print(season_year)

columns_names = []
team_stats = []

for line_rank, lines in enumerate(table_element):
    if line_rank == 0 or line_rank % 5 == 0:
        columns_names.append(lines.split(' '))
    else:
        team_stats.append(lines.split(' '))

print(team_stats)

for content in team_stats:
    if len(content) == 10:
        content.insert(2, ' ')

print(team_stats)
print(columns_names)

db = pd.DataFrame({
    'YEAR': season_year[0],
    'RANK': [i[0] for i in team_stats],
    'TEAM': [i[1] + ' ' + i[2] for i in team_stats],
    'GP': [i[3] for i in team_stats],
    'W': [i[4] for i in team_stats],
    'D': [i[5] for i in team_stats],
    'L': [i[6] for i in team_stats],
    'GF': [i[7] for i in team_stats],
    'GA': [i[8] for i in team_stats],
    'GD': [i[9] for i in team_stats],
    'POINTS': [i[10] for i in team_stats]
})

db = db[['YEAR', 'RANK', 'TEAM', 'GP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'POINTS']]

print(db)

db.to_csv(os.path.join(path, r'2016-2017 UCL Teams Group Stages stats.csv'), index = False)