import re

number = input('Please enter a string with digits: ')

if not re.match(r'^\d+$', number):
    raise TypeError('You are enter invalid argument. Only numbers allowed.')

length = len(number)
index = 0
max_number = None

while index < length:
    char = number[index]

    if max_number is None or int(char) > max_number:
        max_number = int(char)

    index += 1

print(f'Max number from input string is {max_number}.')

