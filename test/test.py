import pandas as pd
import numpy as np
from math import sqrt

list = [1, 2, 3]
list2 = [5, 4, 6]
list3 = [7, 17, 13]

db = pd.DataFrame({
    'C1': list,
    'C2': list2,
    'C3': list3
})

df = pd.DataFrame({
    'col1' : ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2' : [2, 2, 9, 8, 7, 4],
    'col3': [1, 1, 9, 4, 2, 3],
})

print(df)

df3 = df.rename_axis('aaa', axis='rows')
print(df3)