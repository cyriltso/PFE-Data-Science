### Importing libraries ###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import ExcelWriter

### Reading the Dataset ###

dataset = pd.read_csv('/Users/cyriltso/Documents/UCL Statistics/UCL Dataset.csv')
#print(dataset.head(30))

### Switiching the index of the dataframe to the years in order to slice the frames easier for analysis ###

fix_index = dataset.set_index(['YEAR'])

### First interrogation : What are the winnings teams average stats ? ###

    ## UCL Prize List ##

"""
# 2011/2012 : Chelsea                  
# 2012/2013 : Bayern Munich
# 2013/2014 : Real Madrid
# 2014/2015 : FC Barcelona
# 2015/2016 : Real Madrid
# 2016/2017 : Real Madrid
# 2017/2018 : Real Madrid
"""

    ## Stats calculated from the 7 past years ##

select_c1 = fix_index.loc[:, 'W':'GD']
select_c11 = fix_index.loc[:, 'CS%':'AVG']
select_c2 = fix_index.loc[:, 'GOALS':'RATING']

stats_er = select_c1.describe().round(2)
#print(stats_er)

stats_er2 = select_c11.describe().round(2)
#print(stats_er2)

stats_ds = select_c2.describe().round(1)
#print(stats_ds)

    ## Selecting the winning teams ##

        # 2011/2012 : Chelsea #

select_c1 = fix_index.loc['2011/12', 'ROUND':'AVG']
select_c2 = fix_index.loc['2011/12', 'CATEGORIES 1':'RATING']

slicing_1 = select_c1[select_c1.values == 'Chelsea']
slicing_2 = select_c2[select_c2.values == 'Chelsea']

stats_er = slicing_1.loc['2011/12', ['GF', 'GA', 'GD']]

"""
print(stats_er.describe().round(2)) ## Statistics related to the goals ratio
print(slicing_1['W'].value_counts()) ## Total number of wins
print(slicing_1['D'].value_counts()) ## Total number of draws
print(slicing_1['L'].value_counts()) ## Total number of looses
print(slicing_1['CS%'].value_counts()) ## Total number of looses
print(slicing_1['BTTS%'].value_counts()) ## Total number of looses
print(slicing_1['FTS%'].value_counts()) ## Total number of looses
print(slicing_1['Over 1.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['Over 2.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['AVG'].value_counts()) ## Total number of looses
print(slicing_2['GOALS'].value_counts()) ## Total number of goals scored in the competition
print(slicing_2['SHOTS'].value_counts()) ## Average number of shots attempted per match
print(slicing_2['YELLOW CARD'].value_counts()) ## Total number of yellow cards
print(slicing_2['RED CARD'].value_counts()) ## Total number of red cards
print(slicing_2['POSSESSION'].value_counts()) ## Average percentage of possession
print(slicing_2['PASS%'].value_counts()) ## Pass accuracy percentage
print(slicing_2['RATING'].value_counts()) ## Rating
"""

    # 2012/2013 : Bayern Munich #

select_c1 = fix_index.loc['2012/13', 'ROUND':'AVG']
select_c2 = fix_index.loc['2012/13', 'CATEGORIES 1':'RATING']

slicing_1 = select_c1[select_c1.values == 'Bayern Munich']
slicing_2 = select_c2[select_c2.values == 'Bayern Munich']

stats_er = slicing_1.loc['2012/13', ['GF', 'GA', 'GD']]

"""
print(stats_er.describe().round(2)) ## Statistics related to the goals ratio
print(slicing_1['W'].value_counts()) ## Total number of wins
print(slicing_1['D'].value_counts()) ## Total number of draws
print(slicing_1['L'].value_counts()) ## Total number of looses
print(slicing_1['CS%'].value_counts()) ## Total number of looses
print(slicing_1['BTTS%'].value_counts()) ## Total number of looses
print(slicing_1['FTS%'].value_counts()) ## Total number of looses
print(slicing_1['Over 1.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['Over 2.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['AVG'].value_counts()) ## Total number of looses
print(slicing_2['GOALS'].value_counts()) ## Total number of goals scored in the competition
print(slicing_2['SHOTS'].value_counts()) ## Average number of shots attempted per match
print(slicing_2['YELLOW CARD'].value_counts()) ## Total number of yellow cards
print(slicing_2['RED CARD'].value_counts()) ## Total number of red cards
print(slicing_2['POSSESSION'].value_counts()) ## Average percentage of possession
print(slicing_2['PASS%'].value_counts()) ## Pass accuracy percentage
print(slicing_2['RATING'].value_counts()) ## Rating
"""

    # 2013/2014 : Real Madrid #

select_c1 = fix_index.loc['2013/14', 'ROUND':'AVG']
select_c2 = fix_index.loc['2013/14', 'CATEGORIES 1':'RATING']

slicing_1 = select_c1[select_c1.values == 'Real Madrid']
slicing_2 = select_c2[select_c2.values == 'Real Madrid']

stats_er = slicing_1.loc['2013/14', ['GF', 'GA', 'GD']]

"""
print(stats_er.describe().round(2)) ## Statistics related to the goals ratio
print(slicing_1['W'].value_counts()) ## Total number of wins
print(slicing_1['D'].value_counts()) ## Total number of draws
print(slicing_1['L'].value_counts()) ## Total number of looses
print(slicing_1['CS%'].value_counts()) ## Total number of looses
print(slicing_1['BTTS%'].value_counts()) ## Total number of looses
print(slicing_1['FTS%'].value_counts()) ## Total number of looses
print(slicing_1['Over 1.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['Over 2.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['AVG'].value_counts()) ## Total number of looses
print(slicing_2['GOALS'].value_counts()) ## Total number of goals scored in the competition
print(slicing_2['SHOTS'].value_counts()) ## Average number of shots attempted per match
print(slicing_2['YELLOW CARD'].value_counts()) ## Total number of yellow cards
print(slicing_2['RED CARD'].value_counts()) ## Total number of red cards
print(slicing_2['POSSESSION'].value_counts()) ## Average percentage of possession
print(slicing_2['PASS%'].value_counts()) ## Pass accuracy percentage
print(slicing_2['RATING'].value_counts()) ## Rating
"""

    # 2014/2015 : FC Barcelona #

select_c1 = fix_index.loc['2014/15', 'ROUND':'AVG']
select_c2 = fix_index.loc['2014/15', 'CATEGORIES 1':'RATING']

slicing_1 = select_c1[select_c1.values == 'FC Barcelona']
slicing_2 = select_c2[select_c2.values == 'FC Barcelona']

stats_er = slicing_1.loc['2014/15', ['GF', 'GA', 'GD']]

"""
print(stats_er.describe().round(2)) ## Statistics related to the goals ratio
print(slicing_1['W'].value_counts()) ## Total number of wins
print(slicing_1['D'].value_counts()) ## Total number of draws
print(slicing_1['L'].value_counts()) ## Total number of looses
print(slicing_1['CS%'].value_counts()) ## Total number of looses
print(slicing_1['BTTS%'].value_counts()) ## Total number of looses
print(slicing_1['FTS%'].value_counts()) ## Total number of looses
print(slicing_1['Over 1.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['Over 2.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['AVG'].value_counts()) ## Total number of looses
print(slicing_2['GOALS'].value_counts()) ## Total number of goals scored in the competition
print(slicing_2['SHOTS'].value_counts()) ## Average number of shots attempted per match
print(slicing_2['YELLOW CARD'].value_counts()) ## Total number of yellow cards
print(slicing_2['RED CARD'].value_counts()) ## Total number of red cards
print(slicing_2['POSSESSION'].value_counts()) ## Average percentage of possession
print(slicing_2['PASS%'].value_counts()) ## Pass accuracy percentage
print(slicing_2['RATING'].value_counts()) ## Rating
"""

    # 2015/2016 : Real Madrid #

select_c1 = fix_index.loc['2015/16', 'ROUND':'AVG']
select_c2 = fix_index.loc['2015/16', 'CATEGORIES 1':'RATING']

slicing_1 = select_c1[select_c1.values == 'Real Madrid']
slicing_2 = select_c2[select_c2.values == 'Real Madrid']

stats_er = slicing_1.loc['2015/16', ['GF', 'GA', 'GD']]

"""
print(stats_er.describe().round(2)) ## Statistics related to the goals ratio
print(slicing_1['W'].value_counts()) ## Total number of wins
print(slicing_1['D'].value_counts()) ## Total number of draws
print(slicing_1['L'].value_counts()) ## Total number of looses
print(slicing_1['CS%'].value_counts()) ## Total number of looses
print(slicing_1['BTTS%'].value_counts()) ## Total number of looses
print(slicing_1['FTS%'].value_counts()) ## Total number of looses
print(slicing_1['Over 1.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['Over 2.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['AVG'].value_counts()) ## Total number of looses
print(slicing_2['GOALS'].value_counts()) ## Total number of goals scored in the competition
print(slicing_2['SHOTS'].value_counts()) ## Average number of shots attempted per match
print(slicing_2['YELLOW CARD'].value_counts()) ## Total number of yellow cards
print(slicing_2['RED CARD'].value_counts()) ## Total number of red cards
print(slicing_2['POSSESSION'].value_counts()) ## Average percentage of possession
print(slicing_2['PASS%'].value_counts()) ## Pass accuracy percentage
print(slicing_2['RATING'].value_counts()) ## Rating
"""

    # 2016/2017 : Real Madrid #

select_c1 = fix_index.loc['2016/17', 'ROUND':'AVG']
select_c2 = fix_index.loc['2016/17', 'CATEGORIES 1':'RATING']

slicing_1 = select_c1[select_c1.values == 'Real Madrid']
slicing_2 = select_c2[select_c2.values == 'Real Madrid']

stats_er = slicing_1.loc['2016/17', ['GF', 'GA', 'GD']]

"""
print(stats_er.describe().round(2))  ## Statistics related to the goals ratio
print(slicing_1['W'].value_counts())  ## Total number of wins
print(slicing_1['D'].value_counts())  ## Total number of draws
print(slicing_1['L'].value_counts())  ## Total number of looses
print(slicing_1['CS%'].value_counts()) ## Total number of looses
print(slicing_1['BTTS%'].value_counts()) ## Total number of looses
print(slicing_1['FTS%'].value_counts()) ## Total number of looses
print(slicing_1['Over 1.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['Over 2.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['AVG'].value_counts())  ## Total number of looses
print(slicing_2['GOALS'].value_counts())  ## Total number of goals scored in the competition
print(slicing_2['SHOTS'].value_counts())  ## Average number of shots attempted per match
print(slicing_2['YELLOW CARD'].value_counts())  ## Total number of yellow cards
print(slicing_2['RED CARD'].value_counts())  ## Total number of red cards
print(slicing_2['POSSESSION'].value_counts())  ## Average percentage of possession
print(slicing_2['PASS%'].value_counts())  ## Pass accuracy percentage
print(slicing_2['RATING'].value_counts())  ## Rating
"""

    # 2017/2018 : Real Madrid #

select_c1 = fix_index.loc['2017/18', 'ROUND':'AVG']
select_c2 = fix_index.loc['2017/18', 'CATEGORIES 1':'RATING']

slicing_1 = select_c1[select_c1.values == 'Real Madrid']
slicing_2 = select_c2[select_c2.values == 'Real Madrid']

stats_er = slicing_1.loc['2017/18', ['GF', 'GA', 'GD']]

"""
print(stats_er.describe().round(2))  ## Statistics related to the goals ratio
print(slicing_1['W'].value_counts())  ## Total number of wins
print(slicing_1['D'].value_counts())  ## Total number of draws
print(slicing_1['L'].value_counts())  ## Total number of looses
print(slicing_1['CS%'].value_counts()) ## Total number of looses
print(slicing_1['BTTS%'].value_counts()) ## Total number of looses
print(slicing_1['FTS%'].value_counts()) ## Total number of looses
print(slicing_1['Over 1.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['Over 2.5+ %'].value_counts()) ## Total number of looses
print(slicing_1['AVG'].value_counts())  ## Total number of looses
print(slicing_2['GOALS'].value_counts())  ## Total number of goals scored in the competition
print(slicing_2['SHOTS'].value_counts())  ## Average number of shots attempted per match
print(slicing_2['YELLOW CARD'].value_counts())  ## Total number of yellow cards
print(slicing_2['RED CARD'].value_counts())  ## Total number of red cards
print(slicing_2['POSSESSION'].value_counts())  ## Average percentage of possession
print(slicing_2['PASS%'].value_counts())  ## Pass accuracy percentage
print(slicing_2['RATING'].value_counts())  ## Rating
"""

### Data Visualization ###

reset = fix_index.reset_index()  # need to cancel the index in order to split each winner line

    ## Features Heatmap ##

"""
        # Teams Playstyle #
        
f_correlation = sns.heatmap(
    fix_index.loc[:, ['CS%', 'BTTS%', 'FTS%', 'Over 1.5+ %', 'Over 2.5+ %', 'AVG']].corr(),
    annot=True
)

        # Teams Offensive Features #

f_correlation2 = sns.heatmap(
    fix_index.loc[:, ['GOALS', 'SHOTS', 'POSSESSION', 'PASS%', 'GF']].corr(),
    annot=True
)

        # Teams Defensive Features #

f_correlation3 = sns.heatmap(
    fix_index.loc[:, ['CS%', 'BTTS%', 'FTS%', 'GA', 'YELLOW CARD', 'RED CARD', 'SHOTS', 'GOALS']].corr(),
    annot=True
)

plt.show()
"""

    ## Mean Calculus ##

visualize = reset.loc[:, ['BTTS%','FTS%', 'Over 1.5+ %', 'Over 2.5+ %', 'YELLOW CARD', 'RED CARD']].mean()
#plot = visualize.plot.hexbin(x='SHOTS', y='GOALS', gridsize=15)
print(visualize)

    ## Mean of offensive stats for the UCL Winning Teams 2011/2018 compared to the others ##

visualize2 = reset.loc[[0, 30, 60, 91, 120, 150, 182], 'TEAM DS':'PASS%']
#plot2 = visualize2.plot.scatter(x='SHOTS', y='GOALS')
#print(visualize2)
#plt.show()

df2 = pd.DataFrame({
    'TEAM DS': 'Mean of other teams',
    'GOALS': [12.0],
    'SHOTS': [13.1],
    'YELLOW CARD': [15.6],
    'RED CARD': [0.7],
    'POSSESSION': [49.9],
    'PASS%': [81.4],
})

to_analyze2 = visualize2.append(df2)

#print(to_analyze2)

    ## Mean of defensive stats for the UCL Winning Teams 2011/2018 compared to the others ##

visualize31 = reset.loc[[28, 58, 88, 118, 148, 178, 208], ['TEAM ER', 'BTTS%', 'FTS%', 'Over 1.5+ %', 'Over 2.5+ %']]
print(visualize31)

visualize32 = reset.loc[[0, 30, 60, 91, 120, 150, 182], ['TEAM DS', 'YELLOW CARD', 'RED CARD']]
visualize32 = visualize32[['YELLOW CARD', 'RED CARD']]
print(visualize32)

visualize321 = visualize31.join([visualize32])
print(visualize321)

df3 = pd.DataFrame({
    'TEAM ER': 'Other teams average',
    'BTTS%': [50.81],
    'FTS%': [18.22],
    'Over 1.5+ %': [79.98],
    'Over 2.5+ %': [58.85],
    'YELLOW CARD': [15.56],
    'RED CARD': [0.71]
})

to_analyze3 = visualize321.append(df3)
print(to_analyze3)


    ## Line plot to compare statistics between the winners and the other teams ##

select = reset.loc[[28, 58, 88, 118, 148, 178, 208], 'YEAR':'AVG']
group = select.groupby('TEAM ER')

total = reset.loc[:, 'YEAR':'AVG'].mean()

df = pd.DataFrame({
    'YEAR': ' ',
    'ROUND': 'Finals',
    'RANK ER': [6.16],
    'TEAM ER': 'ALL TEAMS',
    'MP': [1.93],
    'W': [0.78],
    'D': [0.38],
    'L': [0.78],
    'GF': [2.88],
    'GA': [2.89],
    'GD': [0.01],
    'Last 5': 'W',
    'CS%': [37.93],
    'BTTS%': [50.81],
    'FTS%': [18.22],
    'Over 1.5+ %': [79.98],
    'Over 2.5+ %': [58.85],
    'AVG': [2.98]
})

to_analyze = select.append(df)

group_2 = to_analyze.groupby('TEAM ER')[['CS%', 'BTTS%', 'FTS%', 'Over 1.5+ %', 'AVG']]
#group_2.plot.line()

#print(select.shape)
#print(group.size())
#print(total)
#print(df.shape)
#print(to_analyze)
#print(group_2.size())

#plt.show()

### Using Excel to do the graphs as they are prettier than the one from Matplotlib

writer = ExcelWriter('Graph Analyzing stats.xlsx')
to_analyze3.to_excel(writer, 'Winners vs Mean stats')
writer.save()



