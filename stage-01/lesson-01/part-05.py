import re

proceeds = input('Please enter you proceeds: ')
expenses = input('Please enter you expenses: ')

pattern = r'^\d+$'

if not re.match(pattern, proceeds) or not re.match(pattern, expenses):
    raise TypeError('You are enter input proceeds or expenses. Please verify and try again.')

profit = int(proceeds) - int(expenses)

if profit < 0:
    print('Sorry, but you working at a loos ;(')
    exit(0)

print('Very well, you have profit %d' % profit)

number_of_employers = input('Please enter a number of employers in you company: ')

if not re.match(pattern, number_of_employers):
    raise TypeError(f'You profit is {profit} but we can\'t calculate profit per one employee. Wrong input employers.')

profit_per_one_employee = float(profit / int(number_of_employers))

print('Very well, each employee has %.2f profit for you company.' % profit_per_one_employee)
