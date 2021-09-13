import re


class ElementNotNumberError(Exception):
    pass


def check_element_for_add_to_list(el) -> float:
    if not re.match(r'\d+(\.\d+)?', el):
        raise ElementNotNumberError('The element {} is not a numeric.'.format(el))

    return float(el)


list_elements = []

while True:
    input_element = input('Please enter a element of list: ')

    if input_element == 'stop':
        print('Input list is: {}'.format(list_elements))
        exit(0)

    try:
        list_elements.append(check_element_for_add_to_list(input_element))
    except ElementNotNumberError:
        print('Only numeric allowed')
