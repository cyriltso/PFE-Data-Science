from selenium import webdriver
import pandas as pd
import os

chro_path = '/Users/cyriltso/Documents/UCL Statistics/chromedriver'

browser = webdriver.Chrome(os.path.join(os.getcwd(), chro_path))

path = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Round of 16"

url = 'https://footystats.org/europe/uefa-champions-league/2016-2017/overview'
browser.get(url)

table = browser.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/div/div[8]/div[1]/table')

table_element = table.text.split('\n')

print(table_element)

season = browser.find_element_by_xpath('//*[@id="teamSummary"]/div/div[4]/div[2]')
season_year = season.text.split('\n')
print(season_year)

# columns' names ---> 0 to 26
# ranks ---> 27, 30, 33
# teams ---> 27, 30, 33
# stats ---> all cases

team_all = []
team_stat_1 = []
team_stat_2 = []

for line_num, line_content in enumerate(table_element):
    if 0 <= line_num <= 26:
        pass
    else:
        if line_num % 3 == 0:
            team_all.append(line_content.split(' '))
        if line_num % 3 == 1:
            team_stat_1.append(line_content)
        if line_num % 3 == 2:
            team_stat_2.append(line_content.split(' '))


print(team_all)
print(team_stat_1)
print(team_stat_2)

for content in team_all:
    if len(content) == 10:
        content.insert(3, ' ')
        content.insert(4, ' ')
    elif len(content) == 11:
        content.insert(4, ' ')

print(team_all)

db = pd.DataFrame({
    'YEAR': season_year[0].strip(' '),
    'ROUND': '8th Finals',
    'RANK': [i[0] for i in team_all],
    'TEAM': [i[1] + ' ' + i[2] + ' ' + i[3] + ' ' + i[4] for i in team_all],
    'MP': [i[5] for i in team_all],
    'W': [i[6] for i in team_all],
    'D': [i[7] for i in team_all],
    'L': [i[8] for i in team_all],
    'GF': [i[9] for i in team_all],
    'GA': [i[10] for i in team_all],
    'GD': [i[11] for i in team_all],
    'Last 5': team_stat_1,
    'CS': [i[1] for i in team_stat_2],
    'BTTS': [i[2] for i in team_stat_2],
    'FTS': [i[3] for i in team_stat_2],
    'Over 1.5+': [i[4] for i in team_stat_2],
    'Over 2.5+': [i[5] for i in team_stat_2],
    'AVG': [i[6] for i in team_stat_2]
})

db = db[[
    'YEAR', 'ROUND', 'RANK', 'TEAM', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Last 5',
    'CS', 'BTTS', 'FTS', 'Over 1.5+', 'Over 2.5+', 'AVG'
]]

print(db)

db.to_csv(os.path.join(path, r'2016-2017 UCL Teams 8th Finals stats.csv'), index = False)