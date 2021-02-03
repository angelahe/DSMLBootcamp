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
