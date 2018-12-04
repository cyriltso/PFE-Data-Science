import pandas as pd

list = [1, 2, 3]
list2 = [4, 5, 6]

db = pd.DataFrame({
    'C1': list,
    'C2': list2
})

db2 = pd.DataFrame({
    'C1': list2,
    'C2': list
})

db3 = pd.concat([db,db2], ignore_index = True)

print(db)
print(db2)
print(db3)

listtest = [['1', 'Arsenal', ' ', '6', '4', '2', '0', '18', '6', '+12', '14'], ['2', 'Paris', 'Saint-Germain', '6', '3', '3', '0', '13', '7', '+6', '12']]
print(listtest)

test = []

for i, j in listtest:
    if i % 2 == 1:
        test.append('GROUPE A').append(j)
    elif i % 2 == 0:
        test.append('GROUPE B').append(j)

print(test)
