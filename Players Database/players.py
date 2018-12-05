import pandas as pd
import os

path = "/Users/cyriltso/Documents/UCL Statistics/Players Database/Databases"

scorers = "/Users/cyriltso/Documents/UCL Statistics/Players Stats/Best Scorers/2016-2017 UCL Best Scorers stats.csv"
assists = "/Users/cyriltso/Documents/UCL Statistics/Players Stats/Best assists players/2016-2017 UCL Best Assists players stats.csv"

df1 = pd.read_csv(scorers, usecols = ['YEAR', 'CATEGORIES 1', 'RANK_S', 'NAME_S', 'TEAM_S', 'P_S', 'G'])
df2 = pd.read_csv(assists, usecols = ['CATEGORIES 2', 'RANK_A', 'NAME_A', 'TEAM_A', 'P_A', 'A'])

final_db = df1.join(df2)
print(final_db)

final_db.to_csv(os.path.join(path, r'2016-2017 UCL Players stats.csv'), index = False)