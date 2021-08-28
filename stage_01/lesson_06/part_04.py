class Car:
    def __init__(self, speed: int, color: str, name: str, police: bool):
        self._speed = speed
        self._color = color
        self._name = name
        self._police = police

    def show_speed(self) -> None:
        print(f'Active speed of car {self._name} is {self._speed}')

    def go(self) -> None:
        print(f'The card {self._name} is running.')

    def stop(self) -> None:
        print(f'The car {self._name} stopped.')

    def turn(self, direction) -> None:
        print(f'The car {self._name} turn to {direction}.')


class TownCar(Car):
    def show_speed(self) -> None:
        if self._speed > 60:
            print('The car override speed limit - 60.')

        Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self) -> None:
        if self._speed > 40:
            print('The car override speed limit - 40.')

        Car.show_speed(self)


class PoliceCar(Car):
    pass


def run_and_debug_car(car: Car) -> None:
    car.go()
    car.turn('left')
    car.turn('down')
    car.turn('right')
    car.turn('up')
    car.show_speed()
    car.stop()

    print('')


run_and_debug_car(SportCar(150, 'green', 'Mazda 3', False))
run_and_debug_car(TownCar(80, 'black', 'Kia', False))
run_and_debug_car(WorkCar(40, 'gray', 'Honda', False))
