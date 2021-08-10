import math
from math import ceil

def swap_items(data):
    """
    :param list data: The input list for swap
    """
    if not isinstance(data, (list, tuple)):
        raise TypeError(f'Only list or tuple supported, but {type(data)} given.')

    iterations = math.ceil(len(data) / 2)
    swaps = []

    for iteration in range(0, iterations):
        start_index = iteration * 2

        swaps.append(data[start_index:start_index + 2])

    swapped_data = []

    for swap in swaps: # type: list[any]
        swap.reverse()
        swapped_data.extend(swap)

    return swapped_data


if __name__ == '__main__':
    input_list = []

    while True:
        element = input('Please enter a element of list (for end please enter "end"): ')

        if element == 'end':
            break

        input_list.append(element)

    swapped_items = swap_items(input_list)

    print(f'Input list is: {input_list}')
    print(f'Swapped list is: {swapped_items}')
