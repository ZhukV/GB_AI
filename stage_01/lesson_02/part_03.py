import re

months_in_list = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

months_in_dict = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}


def validate_month(month):
    if not isinstance(month, int):
        raise TypeError(f'Only int supported, but "{type(month)}" given.')

    if month < 1 or month > 12:
        raise ValueError(f'Month must be between 1 and 12, but {month} given.')


def convert_month_from_list(month):
    """
    :param int month: The month (between 1 and 12)
    """
    validate_month(month)

    return months_in_list[month - 1]


def convert_month_from_dict(month):
    """
    :param int month: The month between 1 and 12
    """
    validate_month(month)

    return months_in_dict[str(month)]


if __name__ == '__main__':
    month = input('Please enter a month (between 1 an 12): ')

    if not re.match(r'^\d{1,2}$', month):
        raise ValueError('You are enter invalid month. Only 1 to 12 supported.')

    month_name = convert_month_from_list(int(month))

    print(f'You enter {month} and it name {month_name}')
