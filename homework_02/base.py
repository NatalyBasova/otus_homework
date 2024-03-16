from abc import ABC, abstractmethod
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(
        self,
        weight: int = 0,
        fuel: int = 0,
        fuel_consumption: int = 0,
        started: bool = False,
    ):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    # weight: int
    # started: bool
    # fuel: int
    # fuel_consumption: int

    # def start(self, started, fuel):
    #   if fuel = 0 in started is False:
    #       else:
    #         raise LowFuelError

    #     return started

    # def move(self, fuel, fuel_consumption):
    #     if self.fuel = fuel
    # fuel_consumption > 0
    #         raise NotEnoughFuel

    #     return fuel
