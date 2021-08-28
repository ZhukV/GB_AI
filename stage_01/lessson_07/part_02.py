from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def tissue_consumption(self) -> float:
        pass


class Coat(Clothes):
    def __init__(self, width: int):
        self.__width = width

    @property
    def tissue_consumption(self) -> float:
        return self.__width / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height: int):
        self.__height = height

    @property
    def tissue_consumption(self) -> float:
        return self.__height * 2 + 0.3


coat = Coat(5)
costume = Costume(2)

print(f'Tissue for coat: {coat.tissue_consumption}')
print(f'Tissue for costume: {costume.tissue_consumption}')
print(f'Total tissue: {coat.tissue_consumption + costume.tissue_consumption}')
