from abc import ABC, abstractmethod


class Stationery(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def draw(self) -> None:
        pass


class Pen(Stationery):
    def draw(self) -> None:
        print('Start drawing via pen')


class Pencil(Stationery):
    def draw(self) -> None:
        print('Start drawing via pencil')


class Handle(Stationery):
    def draw(self) -> None:
        print('Start drawing via maker')


pen = Pen('black pan')
pen.draw()

pencil = Pencil('red pencil')
pencil.draw()

handle = Handle('green maker')
handle.draw()

