import numpy as np

#Creating sample array
arr = np.arange(0,11)

print(f'array from 0 to 10: {arr}')

# getting elements of array is similar to python lists
print(f'element at index 8 is {arr[8]}')
print(f'elements from index 1 to 4: {arr[1:5]}')
print(f'first 5 in the array: {arr[:5]}')
# numpy arrays can broadcast
# ie set a value with an index range
arr[0:5]=100
print(f'setting first 5 in array to 100:\n{arr}')

arr = np.arange(0,11)
slice_of_arr = arr[0:6]
print(f'slice of 0:6 of arr: {slice_of_arr}')

# change slice
slice_of_arr[:] = 99
print(f'changed slice arr to value 99: {slice_of_arr}')

# note the change to the slice get reflected back to the original array
print(f'original arr was changed too:\n {arr}')

# to get a copy, you have to be explicit!
arr_copy = arr.copy()
print(f'explicit copy of array: {arr_copy}')

# index a 2d array
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(f'arr_2d is: {arr_2d}')

# index row
print(f'index 1 row: {arr_2d[1]}')

# Getting individual element value
print(f'get 2nd row 1st element: {arr_2d[1][0]}')

# Format is arr_2d[row][col] or arr_2d[row,col]
# Getting individual element value
print(f'getting 2nd row 1st element: {arr_2d[1][0]}')
# same way of getting element
print(f'getting 2nd row 1st element: {arr_2d[1,0]}')

# 2d array slicing
print(f'top right corner of array: \n{arr_2d[:2,1:]}')

# bottom row
print(f'bottom row: {arr_2d[2]}')
print(f'bottom row: {arr_2d[2,:]}')

# fancy indexing - to select rows or columns out of order
#Set up matrix
arr2d = np.zeros((10,10))

#Length of array
arr_length = arr2d.shape[1]

#Set up array
for i in range(arr_length):
    arr2d[i] = i

print(f'arr2d is: {arr2d}')

print(f'get rows 2, 4, 6, 8: {arr2d[[2,4,6,8]]}')

print(f'get rows in any order: {arr2d[[6,4,2,7]]}')

# selections using brackets
arr = np.arange(1,11)
print(f'array 1 to 10: {arr}')

print(f'arr > 4 is: {arr > 4}')
bool_arr = arr > 4

print(f'getting just the values > 4: {arr[bool_arr]}')

print(f'just the values > 2: {arr[arr>2]}')
x = 3
print(f'values > x: {arr[arr>x]}')

arr_2d = np.arange(50).reshape(5,10)
print(f'5x10 array:\n{arr_2d}')
print(f'get 13, 14, 23, 24 using slice:\n{arr_2d[1:3, 3:5]}')