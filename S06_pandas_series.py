# series

import numpy as np
import pandas as pd

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}

print(f'the series:\n{pd.Series(data=my_list)}')
print(f'the series using labels:\n{pd.Series(data=my_list, index=labels)}')
print(f'series simplified using labels:\n{pd.Series(my_list, labels)}')

print(f'series w numpy array:\n{pd.Series(arr)}')
print(f'series w numpy array and labels:\n{pd.Series(arr, labels)}')

print(f'series using dictionary:\n{pd.Series(d)}')

# note you can put any data type into a pandas series

print(f'series on string datatype:\n{pd.Series(labels)}')
print(f'series on functions:\n{pd.Series([sum, print, len])}')

