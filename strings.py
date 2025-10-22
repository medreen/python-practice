first_string = 'Hello'
string_2 = 'New York'

my_str_3 = """
What a time
To be alive!
"""

#string containing double quote
msg = 'She said "Hello, New York!"'
print(msg)

#escape the ""
msg_esc = '''It\'s cold outside
She said \'Hello, there\''''
print(msg_esc)

#string concatenation
print(first_string + '!' + ' ' + string_2 + '!')

#string concatenation and conversion
num = 2000
print('I was born in the year ' + str(num))
print(type(str(num)))

#augmented assignment operator
name = 'Jane'
age = 40

name_and_age = name
name_and_age += str(age) #--append the name as a string--

print(name_and_age)

#f-string
msg_1 = f'My name is {name} and I am {age} years old!' 
print(msg_1)


#indexing
my_name = 'Medreen'
print(len(my_name))

first_char = my_name[0]
print(first_char)
print(my_name[5])

#negative indexing
last_char = my_name[-4]
print(last_char)

#string slice
country = 'New Jersey'
sliced_string = country[4:8] #--omits the last index-char

print(sliced_string)

#step
mountain = "Everest"
print(mountain[:9:2])

#in 
sent_1 = f'I am a good girl'
print('good' in sent_1) #--returns a boolean

##COMMON METHODS
str_4 = "Engineering"
lower_str = 'MEDICINE'
strip_str = '  jason derulo   '


print(str_4.upper())
print(lower_str.lower())
print(strip_str)
print('Stripped version: ' + strip_str.strip())
print(strip_str.replace('jason', 'Jay'))
print(strip_str.split(' '))
print(strip_str.lstrip(' '))


print(string_2.endswith('York'))
print(string_2.startswith('New'))

print(string_2.find('Hello'))
print(strip_str.find('derulo')) #index of the first occurrence


#checks the number of times the substring has been repeated
sub_stc = "I am a girl, a good girl"
print(sub_stc.count("girl"))
print(sub_stc.rfind("girl"))

#capitalize, title
name = 'kennedy hakulieolo'
print(name.capitalize())
print(name.title())

#islower && isupper
lower = 'pride'
upper = 'LOWKEY'
print(lower.islower())
print(upper.isupper())







 