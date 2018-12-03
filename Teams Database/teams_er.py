import pandas as pd
import os

path = "/Users/cyriltso/Documents/UCL Statistics/Teams Database/Elimination Round"

ro16 = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Round of 16/2016-2017 UCL Teams 8th Finals stats.csv"
qf = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Quarter Final/2016-2017 UCL Teams Quarter Final stats.csv"
sf = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Semi Final/2016-2017 UCL Teams Semi Final stats.csv"
f = "/Users/cyriltso/Documents/UCL Statistics/Teams' stats/Final/2016-2017 UCL Teams Final stats.csv"

df1 = pd.read_csv(ro16)
df2 = pd.read_csv(qf)
df3 = pd.read_csv(sf)
df4 = pd.read_csv(f)

final_db = pd.concat([df1, df2, df3, df4], ignore_index = True)
print(final_db)

final_db.to_csv(os.path.join(path, r'2016-2017 UCL Teams ER stats.csv'), index = False)
