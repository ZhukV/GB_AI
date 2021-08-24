class Road:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def calculate_weight(self, height: int) -> float:
        return self.width * self.length * height * 25


road = Road(5000, 20)
print(f'Expected weight of road: {road.calculate_weight(5)}')
