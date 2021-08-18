from typing import List, Generator


def search_large_elements(input_list: List[int]) -> Generator:
    return (el for i, el in enumerate(input_list) if i > 0 and el > input_list[i - 1])


our_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = list(search_large_elements(our_list))

print(f'Input list: {our_list}')
print(f'Result list: {result_list}')
