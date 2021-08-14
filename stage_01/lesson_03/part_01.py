import re


def divide_two_numbers(a, b):
    return a / b


if __name__ == '__main__':
    number_one = input('Please enter source number: ')
    divider = input('Please enter divider: ')
    pattern = r'^\d+$'

    if not re.match(pattern, number_one) or not re.match(pattern, divider):
        raise TypeError('Only numbers supported for divide')

    result = None

    try:
        result = divide_two_numbers(int(number_one), int(divider))
    except ZeroDivisionError:
        print('Divide to zero is forbidden.')
        exit(1)

    print(f'Result: {result}')

