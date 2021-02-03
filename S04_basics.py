# basics of python

# math operations
print(f'1 + 1 is {1+1}')
print(f'1 * 3 is {1 * 3}')
print(f'1/2 is {1/2}')
print(f'2 ** 4 is {2 ** 4}')
print(f'4 % 2 is {4 % 2}')
print(f'5 % 2 is {5 % 2}')
print(f'(2 + 3) * (5 + 5) is {(2 + 3) * (5 + 5)}')

# variables
name_of_var = 2

# strings
print('can use single quotes')
print("can also use double quotes")
print("can wrap 'single quotes' here")

# printing
x = 'hello'
print('x is {one}'.format(one=x))
print(f'x is {x}')

# lists
x = [1,2,3]
print(f'list x is {x}')
y = ['hi', 1, [1,2]]
print(f'list y with different types in it: {y}')

my_list = ['a', 'b', 'c']
my_list.append('d')
print(f'my list a b c appended with d is now {my_list}')
print(f'first element of my list: {my_list[0]}')
print(f'element 1 to the end of my list: {my_list[1:]}')
print(f'first element of list: {my_list[:1]}')
my_list[0] = 'NEW'
print(f'edited list: {my_list}')
nest = [1,2,3,[4,5,['target']]]
print(f'nested list: {nest}')
print(f'accessing inside of nested list: {nest[3]}')
print(f'accessing list in nested list: {nest[3][2]}')
print(f'access one element in nested list: {nest[3][2][0]}')
# string is a list
z = 'hello'
print(f'fifth letter of hello is : {z[4]}')
# string slicing
s = 'abcdefghijk'
print(f'from index 0 on of string: {s[0:]}')
print(f'from start up to but not including index 3: {s[:3]}')
print(f'first three letters of string: {s[0:3]}')

# dictionaries
d = {'key1':'item1','key2':'item2'}
print(f"dictionary d is {d} and access value using a key: {d['key1']}")
e = {'k1':[1,2,3]}
print(f"getting list k1 from dictionary e: {e['k1']}")
print(f"getting 2nd value in the k1 list: {e['k1'][1]}")
f = {'k1':{'innerkey':[1,2,3]}}
print(f"get list value from inside nested dictionary{f}: {f['k1']['innerkey'][2]}")

# booleans
valid = True
invalid = False
print(f'valid is {valid} and invalid is {invalid}')

