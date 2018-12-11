import pandas as pd
from math import sqrt

list = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [1, 1, 1, 1]
list4 = [2, 2, 2, 2]

db = pd.DataFrame({
    'C1': list,
    'C2': list2
})

db2 = pd.DataFrame({
    'C3': list3,
    'C4': list4,
})

#db3 = pd.concat([db,db2], ignore_index = True)

print(db)
print(db2)

db4 = db.join(db2)

print(db4)

print(db['C1']/db['C2'])

print(sqrt(10))

print(5*sqrt(40))

print((50+45+40+35+30+25+20+15+10+5)*3)

