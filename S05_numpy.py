# numpy is a linear algebra library for python
# fast because has bindings into C libraries
# numpy arrays in 2 flavors: vectors and matrices
# vectors are 1-d arrays
# matrices are 2-d arrays (but only 1 row or one column)

import numpy as np

# create array by list or list of lists
my_list = [1,2,3]
print(f'my list as an array: {np.array(my_list)}')

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(f'my_matrix as an array:\n {np.array(my_matrix)}')