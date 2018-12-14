from selenium import webdriver
import pandas as pd
import os
import time

chro_path = '/Users/cyriltso/Documents/NBA Statistics/chromedriver'

browser = webdriver.Chrome(os.path.join(os.getcwd(), chro_path))

path = "/Users/cyriltso/Documents/UCL Statistics/test"

url = 'https://www.worldfootball.net/assists/champions-league-2011-2012/'
browser.get(url)

table = browser.find_element_by_xpath('//*[@id="site"]/div[3]/div[1]/div/div[3]/div/table')
time.sleep(4)
table_element = table.text.split('\n')
print(table_element)

players_list = []

for line_rank, lines in enumerate(table_element):
    if line_rank == 0:
        pass
    else:
        players_list.append(lines.split(' '))

print(players_list)

for content in players_list:
    if len(content) == 8:
        pass
    elif len(content) == 7:
        if content[0].isdigit():
            content.insert(4, ' ')
        else:
            content.insert(1, ' ')
    elif len(content) == 6:
        content.insert(0, ' ')
        content.insert(4, ' ')
    elif len(content) == 5:
        content.insert(0, ' ')
        content.insert(2, ' ')
        content.insert(4, ' ')

print(players_list)

df = pd.DataFrame({
    'ASSISTS': 'Assists',
    'RANK_A': [i[0] for i in players_list],
    'NAME_A': [i[2] + ' ' + i[3] for i in players_list],
    'TEAM_A': [i[5] + ' ' + i[6] for i in players_list],
    'A': [i[7] for i in players_list]
})

df = df[[
    'ASSISTS', 'RANK_A', 'NAME_A', 'TEAM_A', 'A'
]]

print(df)

df.to_csv(os.path.join(path, 'test2.csv'), index=False)
