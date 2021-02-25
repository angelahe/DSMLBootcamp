import numpy as np

# array of 10 zeros
zeros = np.zeros(10)
print(zeros)
# array of 10 ones
ones = np.ones(10)
print(f'ten ones: {ones}')
# array of 10 fives
fives = np.ones(10) * 5
fives_2 = np.zeros(10) + 5
print(fives)
# array of integers from 10 to 50
ten_to_fifty = np.arange(10, 51)
print(ten_to_fifty)
# array of even integers from 10 to 50
ten_to_fifty_evens = np.arange(10, 51, 2)
print(ten_to_fifty_evens)
# 3x3 matrix with values from 0 to 8
three_by_three = np.arange(0,9).reshape(3,3)
print(f'three by three:\n {three_by_three}')
# 3x3 identity matrix
identity_3 = np.eye(3)
print(f'identity matrix:\n {identity_3}')
# random num between 0 and 1
print(f'random # between 0 and 1:\n {np.random.rand(1)}')
# 25 random nums sampled from standard normal distribution
print(f'random 25 std normal distn:\n {np.random.randn(25)}')
# matrix from 0.01 to 1.0
print(f'0.01 to 1.0 2d array: {np.arange(1,101).reshape(10,10) /100}')
# array of 20 linearly spaced points between 0 and 1
print(f'20 linearly spaced points:\n {np.linspace(0,1,20)}')

# indexing and selection
matrix = np.arange(1,26).reshape(5,5)
print(f'matrix is:\n{matrix}')
print(f'slice of array: {matrix[2:,1:]}')
print(f'element of array 20: {matrix[3,4]}')
print(f'more array slicing: {matrix[:3,1:2]}')
print(f'get row 5: {matrix[4,:]}')
print(f'get rows 3 and 4: {matrix[3:5,:]}')

print(f'sum of all values in matrix: {matrix.sum()}')
print(f'std deviation of matrix: {matrix.std()}')
print(f'sum of columns in matrix: {matrix.sum(axis=0)}')