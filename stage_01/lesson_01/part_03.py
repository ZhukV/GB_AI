import re

number = input('Please enter the number (only one digit): ')

if not re.match(r'^\d$', number):
    raise TypeError('You are enter invalid number. Only one int digit allowed.')

result = int(number) + int(number * 2) + int(number * 3)

print(f'Result of n + nn + nnn is: {result}')
