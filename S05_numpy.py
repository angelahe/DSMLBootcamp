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

# built in methods for creating arrays
# np.arange - start, stop, step
print(f'create array from 0 to 10: {np.arange(0,11)}')
print(f'create array from 0 to 10 even nos: {np.arange(0,11,2)}')

print(f'create array of zeros: {np.zeros(3)}')
print(f'create matrix of zeros:\n{np.zeros((5,5))}')
print(f'create matrix of ones:\n{np.ones((3,4))}')

# start stop endnumber to get evenly spaced #s between thoses
print(f'create array with start stop endnumber:\n {np.linspace(0, 5, 10)}')

# identity matrix
print(f'identity matrix linear algebra:\n{np.eye(4)}')
