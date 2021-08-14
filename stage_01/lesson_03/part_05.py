import re

total = 0
ended = False

while not ended:
    numbers_str = input('Please enter a numbers separated by space (for stop, please enter "end"): ')
    numbers = numbers_str.split(' ')

    numbers = map(lambda n: str(n).strip(), numbers)
    numbers = filter(lambda n: bool(n), numbers)

    pattern = r'^\d+$'

    for number in numbers:
        if number == 'end':
            ended = True
            break

        if not re.match(pattern, number):
            raise ValueError(f'You are enter invalid number {number}.')

        total += int(number)

    print(f'Total result is: {total}')
