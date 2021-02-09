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

# random number gen universally distributed between 0 and 1
print(f'random numbers: {np.random.rand(5)}')
print(f'random matrix: {np.random.rand(5)}')

# random gaussian distribution
print(f'random numbers gaussian dist: {np.random.randn(2)}')
print(f'random matrix gaussian dist {np.random.randn(4,4)}')

# random integer in a range (low, high, size)
print(f'10 random integers between 1 and 99 {np.random.randint(1,100,10)}')

# reshape a list into a matrix
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(f'array into a 5x5 matrix:\n {arr.reshape(5,5)}')

# finding max and min of the array using numpy
print(f'random array of 10 ints: {ranarr}')
print(f'max random int in ranarr: {ranarr.max()}')
print(f'index value of max random int: {ranarr.argmax()}')
print(f'min random int in ranarr: {ranarr.min()}')
print(f'index value of min random int: {ranarr.argmin()}')

# shape of a vector
print(f'shape of arr: {arr.shape}')
arr = arr.reshape(5,5)
print(f'shape of arr after reshape: {arr.shape}')

# type of array
print(f'type of arr: {arr.dtype}')