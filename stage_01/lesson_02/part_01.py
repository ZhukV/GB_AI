import re

data_string = input('Please enter a string: ')

data_int = input('Please enter a int: ')

if not re.match(r'^\d+$', data_int):
    raise TypeError('Only digits allowed.')

data_float = input('Please enter a float: ')

if not re.match(r'^\d+(\.\d+)?$', data_float):
    raise TypeError('Only numeric allowed.')

data = (data_string, int(data_int), float(data_float))

for el in data:
    print(f'The value is "{el}" with type "{type(el)}"')
