from random import randint
from typing import List

file = 'part_05_output.txt'

def generate_file_with_random_ints() -> None:
    with open(file, 'w') as f:
        for i in range(0, 10):
            decimal = randint(1, 1000)
            f.write(str(decimal) + ' ')


def read_ints_from_file() -> List[int]:
    with open(file, 'r') as f:
        lines = f.read().split('\n')
        lines = filter(lambda el: bool(el), lines)

        decimals = ' '.join(lines).split(' ')
        decimals = filter(lambda el: bool(el), decimals)
        decimals = map(lambda el: int(el), decimals)

        return list(decimals)


generate_file_with_random_ints()
decimals_from_file = read_ints_from_file()

print(f'Sum of decimals in file: {sum(decimals_from_file)}')
