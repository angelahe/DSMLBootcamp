import numpy as np
arr = np.arange(0,10)

# perform operations on arrays
print(f'arr is: {arr}\narr + arr is:\n{arr + arr}')
print(f'arr is: {arr}\narr - arr is:\n{arr - arr}')
print(f'arr is: {arr}\narr * arr is:\n{arr * arr}')
print(f'arr is: {arr}\narr + 100 is:\n{arr + 100}')
print(f'arr is: {arr}\narr ** arr is:\n{arr ** arr}')
print(f'numpy div by 0 gives warning, not error, outputs nan: {arr/arr}')

# universal array functions

print(f'square root of array: {np.sqrt(arr)}')
print(f'exponential (e^) of array: {np.exp(arr)}')
print(f'max of array is (same as arr.max()): {np.max(arr)}')
print(f'sine of array: {np.sin(arr)}')
print(f'logarithm of array: {np.log(arr)}')