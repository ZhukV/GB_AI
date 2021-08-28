from __future__ import annotations
from enum import Enum
from time import sleep


class TrafficState(Enum):
    RED = 'Red'
    YELLOW = 'Yellow'
    GREEN = 'Green'

    def timeout(self) -> int:
        timeouts = {
            TrafficState.RED: 7,
            TrafficState.YELLOW: 2,
            TrafficState.GREEN: 5
        }

        return timeouts[self]

    def next_state(self) -> TrafficState:
        next_states = {
            TrafficState.RED: TrafficState.YELLOW,
            TrafficState.YELLOW: TrafficState.GREEN,
            TrafficState.GREEN: TrafficState.RED
        }

        return next_states[self]


class TrafficLight:
    def __init__(self) -> None:
        self.__color = TrafficState(TrafficState.RED)

    def running(self) -> None:
        while True:
            print(f'Active color: {self.__color}')
            sleep(self.__color.timeout())
            self.__color = self.__color.next_state()


light = TrafficLight()
light.running()
