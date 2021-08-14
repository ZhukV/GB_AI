import re


def exponentiation(number, exp):
    """
    :param int number:
    :param int exp:
    :rtype int:
    """
    if exp < 1:
        raise ValueError(f'Exponent can\'t be less then 1, but {exp} given.')

    result = number

    for _ in range(1, exp):
        result = result * number

    return result


if __name__ == '__main__':
    number = input('Please enter a number: ')
    exponent = input('Please enter a exponent: ')
    pattern = r'^\d+$'

    if not re.match(pattern, number) or not re.match(pattern, exponent):
        raise TypeError('Only digits allowed.')

    result = exponentiation(int(number), int(exponent))

    print(f'Result: {result}')

