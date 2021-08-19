from itertools import count, cycle
from typing import Generator, List


def generate_random_int_list(start: int, iterations: int = 10) -> Generator:
    for i in range(start, start + iterations):
        yield i


def generate_cycled_list(input_list: List, iterations: int = 10) -> Generator:
    cycler = cycle(input_list)

    for _ in range(0, iterations):
        yield next(cycler)


print(list(generate_random_int_list(2, 5)))
print(list(generate_cycled_list([1, 2], 5)))
