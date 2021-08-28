from __future__ import annotations
from typing import Sequence


class Matrix:
    def __init__(self, data: Sequence[Sequence[int]]):
        self.__data = data

    def __str__(self) -> str:
        buffer = ''

        for i in self.__data:
            for j in i:
                buffer += str(j) + ', '

            buffer += '\n'

        return buffer

    def __add__(self, other: Matrix) -> Matrix:
        new_data = []

        for line, i in enumerate(self.__data):
            if line > len(other.__data) - 1:
                raise ValueError(f'The matrix for add not exist {line} line.')

            new_line = []

            for column, j in enumerate(i):
                if column > len(other.__data[line]) - 1:
                    raise ValueError(f'The matrix for add not exist column {column} in {line} line.')

                new_line.append(self.__data[line][column] + other.__data[line][column])

            new_data.append(new_line)

        return Matrix(new_data)


matrix = Matrix(((1, 2, 3), (3, 2, 1)))
matrix = matrix + Matrix(((1, 1, 1), (2, 2, 2)))

print(matrix)
