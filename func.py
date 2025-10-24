def user_age():
    age = input('How old are you? ')
    print(f'I am {age} years old!')
        
my_age = user_age()
print(my_age)#user_age doesn't return a value 
 
def user_name():
    name1 = input('What is your name? ') 
    return f'Hello {name1}!'

my_name = user_name()
print(my_name)

#Decorators
def say_hello():
   name = input('What is your name? ')
   return 'Hello ' + name

def uppercase_decorator(func):
   def wrapper():
       original_func = func()
       modified_func = original_func.upper()
       return modified_func
   return wrapper

say_hello_res = uppercase_decorator(say_hello)

print(say_hello_res())






