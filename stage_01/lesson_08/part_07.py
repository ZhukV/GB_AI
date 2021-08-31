from __future__ import annotations


class Number:
    def __init__(self, data: float):
        self.__data = data

    def __add__(self, other: Number) -> Number:
        return Number(self.__data + other.__data)

    def __sub__(self, other: Number) -> Number:
        return Number(self.__data - other.__data)

    def __mul__(self, other: Number) -> Number:
        return Number(self.__data * other.__data)

    def __truediv__(self, other: Number) -> Number:
        return Number(self.__data / other.__data)

    def __str__(self) -> str:
        return str(self.__data)


number = (Number(10) + Number(100) - Number(30)) / Number(2) * Number(5)

print('The result of math operations: {}'.format(number))
