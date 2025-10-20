print('Hi, there gorg!!')

print('Fruits: ', 'apples', 'pineapples', 'grapes') #you notice that they are not separated by any charcter.

#sep
print('Fruits: ', 'apples', 'mangoes', 'pears', sep=', ')

#end
print('Fruits', end=': ')
print('apples', end=', ')
print('bananas', end=', ')
print('oranges', end=', ')
print('kiwis', end='\n')

#file output
with open('output.txt', 'w') as f:
   print('Hello world!', file=f)

#flush

import time

print('Processing...', end=' ', flush=True) #if flash is set to true it immediately shows up, instead of waiting for a short time.
time.sleep(2)
print('Done!')

#DATA TYPES
age = 90
print(type(age), end='\n')
print(age)

name = 'Larry'
print(name, type(name), sep='\n')

my_dictionary = {'name': 'Jojo', 'age': '5'}
print(my_dictionary, type(my_dictionary), sep='\n')

my_list = [22, 'Kinderjoy', 8902, 'Apples']
print(my_list, type(my_list), sep='\n')

my_tuple = (3, 4, 6)
print(my_tuple, type(my_tuple), sep='\n')

my_set = {4, 5, 7}
print(my_set, type(my_set), sep='\n')

my_complex_var = 3 + 4j
print(my_complex_var, type(my_complex_var), sep='\n')





