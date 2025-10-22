def user_age():
    age = input('How old are you? ')
    print(f'I am {age} years old!')
        
my_age = user_age()
print(my_age)#user_age doesn't return a value 
 
def user_name():
    name = input('What is your name? ') 
    return f'My name is {name}!'

my_name = user_name()
print(my_name)