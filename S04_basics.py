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

# tuples
t = (1,2,3)
# can access tuples like lists
print(f'2nd element in tuple t is {t[1]}')
# but tuples are immutable, so this would give an error
# t[0] = 'NEW'

# sets
my_set = {1,1,1,2,2,2,3,3,3}
print(f'my set is unique: {my_set}')
print(f'unique elements in a list by casting it to a set: {set([1,1,1,1,2,2,2,5,5,5,6,6,6])}')
# add to a set
s = {1,2,3}
s.add(4)
print(f'set was 1,2,3 and added 4 {s}')

# comparison operators
print(f'1 > 2 is {1 > 2}')
print(f'1 < 2 is {1 < 2}')
print(f'1 >= 2 is {1 >= 2}')
print(f'1 == 1 is {1 == 1}')
print(f"'hi' == 'bye' is {'hi' == 'bye'}")

# logic operators
print(f'(1 > 2) and (2 < 3) is {(1 > 2) and (2 < 3)}')
print(f'(1 == 2) or (2 == 3) or (4 == 4) is {(1 == 2) or (2 == 3) or (4 == 4)}')

# if elif else statements
if 1 < 2:
    print('Yep!')

if 1 < 2:
    print('first')
else:
    print('last')

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')

# for loops
seq = [1,2,3,4,5]

for item in seq:
    print(item)

for item in seq:
    print('Yep')

for jelly in seq:
    print(jelly+jelly)

# while loops
i = 1
while i < 5:
    print(f'i is: {i}')
    i = i+1

# range
print(f'range(5) is {range(5)}')
for i in range(5):
    print(i)

print(f'list(range(5) makes a list: {list(range(5))}')