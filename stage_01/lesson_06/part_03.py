class Income:
    """
    A value object for store income data
    """
    def __init__(self, wage: int, bonus: int):
        self._wage = wage
        self._bonus = bonus

    @property
    def total(self) -> int:
        return self._wage + self._bonus


class Worker:
    def __init__(self, name: str, surname: str, position: str, income: Income):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = income

    @property
    def position(self):
        return self._position


class Position(Worker):
    def get_full_name(self) -> str:
        return f'{self._name} {self._surname}'

    def get_total_income(self) -> int:
        return self._income.total


pos = Position('Vitalii', 'Zhuk', 'Developer', Income(1000, 50))

print(f'The employee {pos.get_full_name()} on position {pos.position} has income {pos.get_total_income()}')
