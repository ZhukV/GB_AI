from abc import ABC, abstractmethod
import inspect


class OfficeEquipment(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass


class Printer(OfficeEquipment):
    def name(self) -> str:
        return 'Printer'


class Scanner(OfficeEquipment):
    def name(self) -> str:
        return 'Scanner'


class Xerox(OfficeEquipment):
    def name(self) -> str:
        return 'Xerox'


class WarehouseOfficeEquipment:
    def __init__(self):
        self.__warehouse = {}

    def add(self, other: OfficeEquipment) -> None:
        if not isinstance(other, OfficeEquipment):
            raise ValueError('Only {} allowed for add to warehouse, but {} given.'.format(OfficeEquipment.__name__, type(other)))

        class_name = other.__class__.__name__

        if class_name not in self.__warehouse:
            self.__warehouse[class_name] = []

        self.__warehouse[class_name].append(other)

    def count(self, equipment) -> int:
        if not inspect.isclass(equipment):
            raise TypeError('Only class allowed for get count of equipments')

        class_name = equipment.__name__

        if class_name not in self.__warehouse:
            return 0

        return len(self.__warehouse[class_name])


warehouse = WarehouseOfficeEquipment()

warehouse.add(Printer())
warehouse.add(Printer())
warehouse.add(Xerox())

print('Warehouse contain {} printers.'.format(warehouse.count(Printer)))
print('Warehouse contain {} xeroxs.'.format(warehouse.count(Xerox)))
print('Warehouse contain {} scanners.'.format(warehouse.count(Scanner)))
