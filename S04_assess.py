# what is 7 to the power of 4
print(f'7**2 is : {7**2}')

# split this string into a list
s = 'Hi there Sam!'

splitstring = s.split()
print(f'string split into list: {splitstring}')

planet = "Earth"
diameter = 12742

print(f'the diameter of {planet} is {diameter}')
print('the diameter of {} is {}'.format(planet, diameter))

# get hello from these nested lists:

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(f'getting hello from the list: {lst[3][1][2][0]}')

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(f"get hello again: {d['k1'][3]['tricky'][3]['target'][3]}")

# difference between a list and a tuple
# a tuple is immutable

# function that grabs an email domain from an email address
def getDomain(email):
    return email.split('@')[-1]

domain = getDomain('user@domain.com')
print(f'domain in user@domain.com is {domain}')

def findDog(st):
    return 'dog' in st.lower().split()

print(f"find dog in phrase is there a dog here: {findDog('Is there a dog here?')}")

def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count

print(f"# of times dog is in phrase: {countDog('This dog runs faster than the other dog dude!')}")

# filter out words that don't start with s
seq = ['soup','dog','salad','cat','great']

print(f"s words in the list: {list(filter(lambda word: word[0]=='s',seq))}")

"""
Write a function to return one of 3 possible results: 
"No ticket", "Small ticket", or "Big Ticket". If your speed 
is 60 or less, the result is "No Ticket". If speed is between 
61 and 80 inclusive, the result is "Small Ticket". If speed is 
81 or more, the result is "Big Ticket". Unless it is your 
birthday (encoded as a boolean value in the parameters 
of the function) -- on your birthday, your speed can be 
5 higher in all cases.
"""

def caught_speeding(speed, is_birthday):

    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

print(f"should be no ticket: {caught_speeding(60, False)}")
print(f"should be small ticket: {caught_speeding(81,True)}")
print(f"should be big ticket: {caught_speeding(81,False)}")