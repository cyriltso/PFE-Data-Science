### Importing Librairies ###

from selenium import webdriver
import pandas as pd
import os
import time

### Acquiring data for the advanced stats related to teams from whoscored.com ###

    ## Variables ##

url = 'https://www.whoscored.com/Regions/250/Tournaments/12/Seasons/2944/Stages/6021/TeamStatistics/Europe-UEFA-Champions-League-2011-2012'
year = '2011/12'
name = '2011-2012 UCL Teams Summary stats.csv'

    ## Scraping Algorithm ##

def sum_stats(url, year, name):
    chro_path = '/Users/cyriltso/Documents/UCL Statistics/chromedriver'
    browser = webdriver.Chrome(os.path.join(os.getcwd(), chro_path))

    path = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Detailed stats/"
    browser.get(url)
    time.sleep(4)
    table = browser.find_element_by_xpath('//*[@id="top-team-stats-summary-grid"]')
    table_element = table.text.split('\n')

    print(table_element)

    team_stats = []

    for line_rank, lines in enumerate(table_element):
        if line_rank == 0:
            pass
        else:
            team_stats.append(lines.split(' '))

    print(team_stats)

    for content in team_stats:
        if len(content) == 9:
            content.insert(2, ' ')
        else:
            pass

    print(team_stats)

    db = pd.DataFrame({
        'YEAR': year,
        'VIEW': 'OVERALL',
        'RANK_S': [i[0] for i in team_stats],
        'TEAM_DS': [i[1] + ' ' + i[2] for i in team_stats],
        'GOALS': [i[3] for i in team_stats],
        'SHOTS': [i[4] for i in team_stats],
        'DISCIPLINE(Y,R/10)': [i[5] for i in team_stats],
        'POSSESSION': [i[6] for i in team_stats],
        'PASS%': [i[7] for i in team_stats],
        'AW': [i[8] for i in team_stats],
        'RATING': [i[9] for i in team_stats]
    })

    db = db[[
        'YEAR', 'VIEW', 'RANK_S', 'TEAM_DS', 'GOALS', 'SHOTS', 'DISCIPLINE(Y,R/10)',
        'POSSESSION', 'PASS%', 'AW', 'RATING'
    ]]

    print(db)

    db.to_csv(os.path.join(path, name), index = False)

#sum_stats(url, year, name)

### Acquiring data for the teams' stats from footystats.org ###

    ## Variables ##

url = 'https://footystats.org/europe/uefa-champions-league/2013-2014/overview'
path = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Round of 16"
year = '2013/14'
round = '8th Finals'
xpath = '//*[@id="content"]/div[3]/div[3]/div/div[9]/div[1]/table'
file_path = '2013-2014 UCL Teams 8th Final stats.csv'

    ## Scraping Algorithm ##

def team_stats(url, path, year, round, xpath, file_path):
    chro_path = '/Users/cyriltso/Documents/UCL Statistics/chromedriver'
    browser = webdriver.Chrome(os.path.join(os.getcwd(), chro_path))

    browser.get(url)
    time.sleep(4)
    table = browser.find_element_by_xpath(xpath)
    table_element = table.text.split('\n')

    print(table_element)

    """
    season = browser.find_element_by_xpath('//*[@id="teamSummary"]/div/div[4]/div[2]')
    season_year = season.text.split('\n')
    print(season_year)
    """

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
        if len(content) == 9:
            content.insert(2, ' ')
            content.insert(3, ' ')
            content.insert(4, ' ')
        elif len(content) == 10:
            content.insert(3, ' ')
            content.insert(4, ' ')
        elif len(content) == 11:
            content.insert(4, ' ')

    print(team_all)

    db = pd.DataFrame({
        'YEAR': year,
        'ROUND': round,
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

    db.to_csv(os.path.join(path, file_path), index=False)

#team_stats(url, path, year, round, xpath, file_path)

### Acquiring data related to the best players from espn.com ###

    ## Variables 1 ##

url_s = 'http://www.espn.com/soccer/stats/_/league/UEFA.CHAMPIONS/season/2011'
path_s = "/Users/cyriltso/Documents/UCL Statistics/Players Stats/Best Scorers"
xpath_s = '//*[@id="fittPageContainer"]/div[3]/div[1]/div[1]/article/div/article/div/section/div/div[1]/section/section/' \
        'table/tbody/tr/td/div/div/div[2]/table/tbody/tr/td/table'
year_s = '2011/12'
file_s = '2011-2012 UCL Best Scorers stats.csv'

    ## Scraping Algorithm for the scorers ##

def scorers(url, path, xpath, year, file):
    chro_path = '/Users/cyriltso/Documents/UCL Statistics/chromedriver'
    browser = webdriver.Chrome(os.path.join(os.getcwd(), chro_path))
    browser.get(url)
    time.sleep(4)

    table = browser.find_element_by_xpath(xpath)
    table_element = table.text.split('\n')

    print(table_element)

    """
    season = browser.find_element_by_xpath(
        '//*[@id="fittPageContainer"]/div[3]/div[1]/div[1]/article/div/article/div/div[3]/select[1]')
    season_year = season.text.split('\n')
    print(season_year)
    """

    players_specs = []

    for line_rank, lines in enumerate(table_element):
        if line_rank == 0:
            pass
        else:
            players_specs.append(lines.split(' '))

    print(players_specs)

    for content in players_specs:
        if len(content) == 8:
            content.insert(0, ' ')
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
        'YEAR': year,
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

    db.to_csv(os.path.join(path, file), index=False)

#scorers(url_s, path_s, xpath_s, year_s, file_s)

    ## Variables 2 ##

url_a = 'http://www.espn.com/soccer/stats/_/league/UEFA.CHAMPIONS/season/2012'
path_a = "/Users/cyriltso/Documents/UCL Statistics/Players Stats/Best assists players"
xpath_a = '//*[@id="fittPageContainer"]/div[3]/div[1]/div[1]/article/div/article/div/section/div/div[2]/section/' \
          'section/table'
year_a = '2012/13'
file_a = '2012-2013 UCL Best Passers stats.csv'

    ## Scraping Algorithms for the passers ##

def assists(url, path, xpath, year, file):
    chro_path = '/Users/cyriltso/Documents/UCL Statistics/chromedriver'
    browser = webdriver.Chrome(os.path.join(os.getcwd(), chro_path))
    browser.get(url)
    time.sleep(4)

    table = browser.find_element_by_xpath(xpath)
    table_element = table.text.split('\n')

    print(table_element)

    """
    season = browser.find_element_by_xpath(
        '//*[@id="fittPageContainer"]/div[3]/div[1]/div[1]/article/div/article/div/div[3]/select[1]')
    season_year = season.text.split('\n')
    print(season_year)
    """

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
        'YEAR': year,
        'CATEGORIES 2': 'Assists',
        'RANK_A': [i[0] for i in players_specs],
        'NAME_A': [i[1] + ' ' + i[2] for i in players_specs],
        'TEAM_A': [i[3] + ' ' + i[4] for i in players_specs],
        'P_A': [i[5] for i in players_specs],
        'A': [i[6] for i in players_specs],
    })

    db = db[[
        'YEAR', 'CATEGORIES 2', 'RANK_A', 'NAME_A', 'TEAM_A', 'P_A', 'A'
    ]]

    print(db)

    db.to_csv(os.path.join(path, file), index=False)

#assists(url_a, path_a, xpath_a, year_a, file_a)

### Concatenate and joining the different dataframes into a single one ###

    ## Variables ##

        # First Concatening #

path_c = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Elimination Round"
ro16 = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Round of 16/2017-2018 UCL Teams 8th Final stats.csv"
qf = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Quarter Final/2017-2018 UCL Teams Quarter Final stats.csv"
sf = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Semi Final/2017-2018 UCL Teams Semi Final stats.csv"
f = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Final/2017-2018 UCL Teams Final stats.csv"
file_name = "2017-2018 UCL Teams ER stats.csv"

        # Second Concatening #

concat_0 = "/Users/cyriltso/Documents/UCL Statistics/Teams Database/Data/2011-2012 UCL Stats.csv"
concat_1 = "/Users/cyriltso/Documents/UCL Statistics/Teams Database/UCL Database.csv"
concat_2 = "/Users/cyriltso/Documents/UCL Statistics/Teams Database/Data/2014-2015 UCL Stats.csv"
concat_3 = "/Users/cyriltso/Documents/UCL Statistics/Teams Database/Data/2015-2016 UCL Stats.csv"
concat_4 = "/Users/cyriltso/Documents/UCL Statistics/Teams Database/Data/2016-2017 UCL Stats.csv"
concat_5 = "/Users/cyriltso/Documents/UCL Statistics/Teams Database/Data/2017-2018 UCL Stats.csv"

file_name_2 = "UCL Dataset_v2.csv"

        # Joining #

path_j = "/Users/cyriltso/Documents/UCL Statistics/Teams Database"
file_join = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Elimination Round/2012-2013 UCL Teams ER stats.csv"
ds = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Detailed stats/2012-2013 UCL Teams Summary stats.csv"
p_join = "/Users/cyriltso/Documents/UCL Statistics/Players Database/Databases/2012-2013 UCL Players Stats.csv"
name = "2012-2013 UCL Stats.csv"

    ## Concatenating the DataFrames ##

def concat(path, p0, p1, f_name):
    df0 = pd.read_csv(p0)
    df1 = pd.read_csv(p1)
    """
    df2 = pd.read_csv(p2)
    df3 = pd.read_csv(p3)
    df4 = pd.read_csv(p4)
    df5 = pd.read_csv(p5)
    """

    final_db = pd.concat([df0, df1], ignore_index=True)
    print(final_db)

    final_db.to_csv(os.path.join(path, f_name), index=False)

concat(path_j, concat_0, concat_1, file_name_2)

    ## Joining the DataFrames ##

def join(path, p1, p2, p3, name):

    df1 = pd.read_csv(p1)

    df2 = pd.read_csv(p2, usecols=[
        'VIEW', 'RANK_S', 'TEAM_DS', 'GOALS', 'SHOTS', 'DISCIPLINE(Y,R/10)', 'POSSESSION', 'PASS%', 'AW', 'RATING'
    ])

    df3 = pd.read_csv(p3, usecols=[
        'CATEGORIES 1', 'RANK_SC', 'NAME_SC', 'TEAM_SC', 'P_SC', 'G', 'CATEGORIES 2', 'RANK_A', 'NAME_A', 'TEAM_A', 'P_A', 'A'
    ])

    db = df1.join(df2).join(df3)

    print(db)

    db.to_csv(os.path.join(path, name), index=False)

#join(path_j, file_join, ds, p_join, name)
