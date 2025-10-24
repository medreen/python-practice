#comparison operators
print(3 <= 6) #less than, equal to\
print(9 == '9')
print(0 > 3)

age = input('How old are you? ')
#conditionals
if int(age) >= 18:
    print('Access Granted')
else:
    print('Access Denied')  

name = input('What is your name? ')      
if name.startswith('M'):
    print('User is valid')
elif name.endswith('n'):
    print('User is valid')
else:
    print('Imposter!!!')    