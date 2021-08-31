from __future__ import annotations
from math import ceil


class Cell:
    def __init__(self, count: int):
        self.__count = count

    def __add__(self, other: Cell) -> Cell:
        return Cell(self.__count + other.__count)

    def __sub__(self, other: Cell) -> Cell:
        result = self.__count - other.__count

        if result < 0:
            return Cell(0)

        return Cell(result)

    def __mul__(self, other: Cell) -> Cell:
        return Cell(self.__count * other.__count)

    def __truediv__(self, other: Cell) -> Cell:
        return Cell(round(self.__count / other.__count))

    def make_order(self, count_in_rows: int) -> str:
        buffer = '*' * self.__count
        rows = ceil(self.__count / count_in_rows)

        result = ''

        for i in range(0, rows):
            result += buffer[i * count_in_rows:i * count_in_rows + count_in_rows] + '\n'

        return result


cell = (Cell(10) + Cell(20)) / Cell(3) * Cell(2)
print(cell.make_order(7))
