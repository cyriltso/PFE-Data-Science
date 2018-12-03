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

