# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Faris'
age = 27

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age)) # would need to cast age because we can't concatenate int

# String Formatting

# Arguemnts by position
#print('My name is {name} and I am {age}'.format(name=name, age=age))
# the formatting above is an alternative to line 7, we're essentially using the curly braces as place holders,
# but would need to call a format method to insert the right variables

# F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')
# This is easier than line 12 or line 7 as you can see, but f-strings is only available in python 3.6 and up
# similar to Javascript template literals

# String Methods

s = 'hello world'

# capitalize string
print(s.capitalize()) # will capitalize the first letter in the string


# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'helloworld'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())