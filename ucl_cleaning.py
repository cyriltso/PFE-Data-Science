### Importing libraries ###

import pandas as pd
import os

### Setting the path to save the dataset ###

path = "/Users/cyriltso/Documents/UCL Statistics"
name = "UCL Dataset.csv"

### Opening and reading the dataset that we want to clean ###

dataset = pd.read_csv('/Users/cyriltso/Documents/UCL Statistics/Teams Database/UCL Dataset_v2.csv')

### Renaming the columns' that are not explicit (like TEAM_A for example) ###

    ## Current columns' name ##

#YEAR,ROUND,RANK,TEAM,MP,W,D,L,GF,GA,GD,Last 5,CS,BTTS,FTS,Over 1.5+,Over 2.5+,AVG,
#VIEW,RANK_S,TEAM_DS,GOALS,SHOTS,"DISCIPLINE(Y,R/10)",POSSESSION,PASS%,AW,RATING,
#CATEGORIES 1,RANK_SC,NAME_SC,TEAM_SC,P_SC,G,
#CATEGORIES 2,RANK_A,NAME_A,TEAM_A,P_A,A

    ## Refactoring the columns ##

cr = dataset.rename(columns = {
    "RANK": "RANK ER",
    "TEAM": "TEAM ER",
    "VIEW": "CATEGORIES 1",
    "RANK_S": "RANK DS",
    "TEAM_DS": "TEAM DS",
    "DISCIPLINE(Y,R/10)": "DISCIPLINE(Y,R)",
    "CATEGORIES 1": "CATEGORIES 2",
    "RANK_SC": "RANK SC",
    "NAME_SC": "NAME SC",
    "TEAM_SC": "TEAM SC",
    "P_SC": "MP SC",
    "CATEGORIES 2": "CATEGORIES 3",
    "RANK_A": "RANK A",
    "NAME_A": "NAME A",
    "TEAM_A": "TEAM A",
    "P_A": "MP A",
    "CS": "CS%",
    "BTTS": "BTTS%",
    "FTS": "FTS%",
    "Over 1.5+": "Over 1.5+ %",
    "Over 2.5+": "Over 2.5+ %"
})

print(cr.shape)

### Homogenizing the teams' names ###

replace = cr.replace(
    ['Bayern München', 'Juventus', 'Paris Saint-Germain FC', 'Manchester United FC', 'Real Madrid CF',
    'Benfica', 'FC Shakhtar Donetsk', 'FC Basel 1893', 'AS Monaco FC', 'Zenit St. Petersburg',
     'Chelsea FC', 'Zenit St.', 'Zenit St.Petersburg', 'Ajax', 'Sevilla', 'Monaco', 'Olympiacos',
     'Napoli', 'Tottenham', 'Roma', 'Valencia', 'Liverpool', 'FC FCSB', 'CFR Cluj', 'Inter', 'Feyenoord',
     'Leicester', 'Gent', 'Genk', 'Braga', 'Wolfsburg', 'St. Petersburg', 'Barcelona', ' Shakhtar Donetsk',
     ' Paris Saint-Germain', 'Tottenham Hotspur', 'Olympique Lyon', 'Olympique Marseille', 'Arsenal FC',
     'CSKA Moskva', ' Zenit St Petersburg', ' Atletico Madrid', 'APOEL Nikosia', ' Valencia', 'Manchester City ', '0%',
     '1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%', '11%', '12%', '13%', '14%', '15%', '16%', '17%',
     '18%', '19%', '20%', '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%', '31%', '32%', '33%', '34%',
     '35%', '36%', '37%', '38%', '39%', '40%', '41%', '42%', '43%', '44%', '45%', '46%', '47%', '48%', '49%', '50%', '51%',
     '52%', '53%', '54%', '55%', '56%', '57%', '58%', '59%', '60%', '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%',
     '69%', '70%', '71%', '72%', '73%', '74%', '75%', '76%', '77%', '78%', '79%', '80%', '81%', '82%', '83%', '84%', '85%',
     '86%', '87%', '88%', '89%', '90%', '91%', '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%', '100%'],

    ['Bayern Munich', 'Juventus FC', 'Paris Saint-Germain', 'Manchester United', 'Real Madrid',
     'SL Benfica', 'Shakhtar Donetsk', 'FC Basel', 'AS Monaco', 'Zenit St Petersburg', 'Chelsea',
     'Zenit St Petersburg', 'Zenit St Petersburg', 'Ajax Amsterdam', 'Sevilla FC', 'AS Monaco',
     'Olympiakos', 'SSC Napoli', 'Tottenham Hotspur FC', 'AS Roma', 'Valencia CF', 'Liverpool FC',
     'Steaua Bucarest', 'CFR Cluj-Napoca', 'Inter Milan', 'Feyenoord Rotterdam', 'Leicester City',
     'KAA Gent', 'KRC Genk', 'Sporting Braga', 'VfL Wolfsburg', 'Zenit St Petersburg', 'FC Barcelona',
     'Shakhtar Donetsk', 'Paris Saint-Germain', 'Tottenham Hotspur FC', 'Lyon', 'Marseille', 'Arsenal',
     'CSKA Moscow', 'Zenit St Petersburg', 'Atletico Madrid', 'APOEL Nicosie', 'Valencia CF', 'Manchester City','0',
     '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
     '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
     '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
     '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67',
     '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84',
     '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
)

### Checking anomalies inside of the dataset ###

    ## Analyzing the columns ##

checking = replace.loc[180:209, "A"]
#print(checking.value_counts())
#print(checking)

    ## Aiming the error area ##

aim = replace.loc[[191],"GOALS":"RATING"]
#print(aim)

    ## Correcting the errors ##

def correct(index, v1, v2, v3, v4, v5, v6, v7):
    replace.loc[[index], "GOALS"] = v1
    replace.loc[[index], "SHOTS"] = v2
    replace.loc[[index], "DISCIPLINE(Y,R)"] = v3
    replace.loc[[index], "POSSESSION"] = v4
    replace.loc[[index], "PASS%"] = v5
    replace.loc[[index], "AW"] = v6
    replace.loc[[index], "RATING"] = v7

def correct_2(index, v):
    replace.loc[[index], "A"] = v

correct(74, '9', '13.4', '161', '55.7', '80.9', '12.1', '6.79')
correct(75, '5', '10', '131', '50.8', '80.6', '14', '6.78')
correct(112, '4', '10', '150', '53.2', '78.9', '19.2', '6.74')
correct(114, '8', '11.9', '222', '46.2', '81.1', '10', '6.67')
correct(132, '14', '10.4', '232', '44.3', '77.3', '16', '6.91')
correct(179, '3', '10.3', '111', '42.6', '80.4', '9.3', '6.43')
correct(191, '13', '10.4', '140', '39.1', '75.7', '11.8', '6.83')

correct_2(60, '5')
correct_2(71, '4')
correct_2(110, '2')

    ## Double checking the column after correction ##

double_check = replace.loc[180:209, "GOALS":"RATING"]
#print(double_check)

### Removing useless data ###

remove = replace.drop(columns=['AW'])

### Switching the index on years and rounds to make frames slicing easier for the analysis ###

#switch_index = remove.set_index('YEAR')

#switch_index['YEAR'] = remove.index
#print(remove)

#test = switch_index.loc[['2013/14'], 'CATEGORIES 1':'RATING']
#print(test)

### Changing the contents of an entire column ###

content_sw = remove.replace(['Scorers', 'Assists'], ['SCORERS', 'ASSISTS'])

#test_2 = content_sw.loc['2011/12', ['CATEGORIES 2','CATEGORIES 3']]
#print(test_2)

### Checking the type of a column in order to avoid inconsistency ###

def check_type(column):
    col = content_sw.loc[:, column]
    type = col.dtype
    print(type)
    return type

#check_type('GOALS')
#check_type('NAME A')
#check_type('MP A')
#check_type('A')

### Changing the dtype on some columns in order to be able to make calculations ###

def change_type_float(column):
    content_sw[column] = content_sw[column].astype('float64')

change_type_float('SHOTS')
change_type_float('POSSESSION')
change_type_float('PASS%')
change_type_float('RATING')

def change_type_int(column):
    content_sw[column] = content_sw[column].astype('int64')

change_type_int('GOALS')
change_type_int('A')
change_type_int('DISCIPLINE(Y,R)')
change_type_int('CS%')
change_type_int('BTTS%')
change_type_int('FTS%')
change_type_int('Over 1.5+ %')
change_type_int('Over 2.5+ %')

"""
content_sw['A'] = content_sw['A'].astype('int64')
content_sw['DISCIPLINE(Y,R)'] = content_sw['DISCIPLINE(Y,R)'].astype('int64')
"""

### Creating new columns ###

    ## ASSISTS RATIO ##

content_sw['ASSISTS RATIO'] = (content_sw['A']/content_sw['MP A']).round(2)

    ## GOALS RATIO ##

content_sw['GOALS RATIO'] = (content_sw['G']/content_sw['MP SC']).round(2)

    ## YELLOW CARD ##

content_sw['YELLOW CARD'] = (content_sw['DISCIPLINE(Y,R)']/10).astype('int64')

    ## RED CARD ##

content_sw['RED CARD'] = (content_sw['DISCIPLINE(Y,R)']%10)

#print(content_sw)

### Reogarnizing the columns order of the DataFrame ###

content_sw = content_sw[[
    'YEAR', 'ROUND', 'RANK ER', 'TEAM ER', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Last 5',
    'CS%', 'BTTS%', 'FTS%', 'Over 1.5+ %', 'Over 2.5+ %', 'AVG', 'CATEGORIES 1', 'RANK DS',
    'TEAM DS', 'GOALS', 'SHOTS', 'YELLOW CARD', 'RED CARD', 'POSSESSION', 'PASS%', 'RATING',
    'CATEGORIES 2', 'RANK SC', 'NAME SC', 'TEAM SC', 'MP SC', 'G', 'GOALS RATIO',
    'CATEGORIES 3', 'RANK A', 'NAME A', 'TEAM A', 'MP A', 'A', 'ASSISTS RATIO'
]]

#print(content_sw)


### Cleaned DataFrame to save ###

content_sw.to_csv(os.path.join(path, name), index=False)
