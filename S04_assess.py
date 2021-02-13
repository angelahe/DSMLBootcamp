# what is 7 to the power of 2
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