class CustomZeroDivisionError(Exception):
    pass


def divide(number: int, divider: int) -> float:
    try:
        return number / divider
    except ZeroDivisionError:
        raise CustomZeroDivisionError('Can\'t divide by zero')


a = int(input('Please enter a number for divide: '))
b = int(input('Please enter a divider: '))

try:
    result = divide(a, b)

    print(f'The result of divide {result}')
except CustomZeroDivisionError:
    print('Can\'t divide by zero.')
