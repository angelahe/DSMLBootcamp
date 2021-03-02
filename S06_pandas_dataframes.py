# dataframes are bunch of series objects put together to share the same index

import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())

print(f'dataframe:\n{df}')

# selection and indexing
print(df['W'])
print(f"type of df['W']: {type(df['W'])}")
print(f"not recommended to use sql syntax:\n{df.W}")
print(f"get W and Z columns:\n {df[['W', 'Z']]}")

# create new column
df['new'] = df['W'] + df['Y']
print(f"with new column:\n{df}")

# remove column, explicitly say inplace so don't accidentally affect the dataframe
df.drop('new', axis=1, inplace=True)
print(f"dropped new column:\n{df}")

# remove a row, axis=0 is the default
print(f"dropped E row:\n{df.drop('E')}")

# because I didn't do inplace, is not permanently dropped from dataframe
print(f'rows,columns:{df.shape}')

# selecting rows
# by label
print(f"select row A: {df.loc['A']}")
# by index
print(f"select row 3 by index:\n{df.iloc[2]}")

# select subset of rows and columns
print(f"one element at B Y: {df.loc['B', 'Y']}")
print(f"slice of elements rows AB, columns WY: {df.loc[['A','B'],['W','Y']]}")