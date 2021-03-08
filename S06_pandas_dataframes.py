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

# conditional selection of dataframes similar to numpy
print(f'dataframe is :\n{df}')
print(f'dataframe > 0:\n{df > 0}')

booldf = df > 0

print(f'value with null where condition not true df > 0:\n{df[booldf]}')

print(f'one step apply condition:\n{df[df>0]}')

print(f"{df[df['W']>0]}")
# two step is:
resultdf = df[df['W']>0]
print(f"{resultdf['Y']}")
# one step is:
print(f"{df[df['W']>0]['Y']}")
print(f"{df[df['Z']<0]}")
print(f"{df[df['W']>0]}")
print(f"{df[df['W']>0]['Y']}")
# mult steps:
boolser = df['W']>0
result = df[boolser]
mycols = ['Y', 'X']
print(f"{result[mycols]}")
# one step
print(f"{df[df['W']>0][['Y','X']]}")

# multiple conditions with and (&)
print(f"{df[(df['W']>0) & (df['Y'] > 1)]}")

# multiple conditions with or (|)
print(f"{df[(df['W']>0) | (df['Y'] > 1)]}")

# reset index
print(f"reset index:\n{df.reset_index()}")
# to do permanently:
# print(f"reset index:\n{df.reset_index(inplace=True)}")

newindex = 'CA NY WY OR CO'.split()
print(f"index list is: {newindex}")

df['States'] = newindex

print(f"new column added to dataframe called states:\n{df}")

# must do inplace=True for this change to be permanent
print(f"set states to be index:\n{df.set_index('States')}")

# multi-index and index hierarchy
# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
# make list of tuple pairs
hier_index = list(zip(outside,inside))
print(f"tuple pairs:\n{hier_index}")
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(f"multi-level labels:\n{hier_index}")

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(f"dataframe is now:\n{df}")

print(f"get G1 sub-dataframe:\n{df.loc['G1']}")

# do outside to inside index (in order)
print(f"get first row of sub-dataframe:\n{df.loc['G1'].loc[1]}")

# give indexes names
print(f'names of indexes before you name them: {df.index.names}')

df.index.names = ['Groups', 'Num']
print(f'dataframe with index names:\n{df}')

print(f"get G2 row 2 column B element:\n{df.loc['G2'].loc[2]['B']}")
print(f"get G1 row 3 column A element:\n{df.loc['G1'].loc[3]['A']}")