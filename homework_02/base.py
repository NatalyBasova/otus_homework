from abc import ABC, abstractmethod
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(
        self,
        weight: int = 0,
        fuel: int = 0,
        fuel_consumption: int = 0,
    ):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

        self.started = False

    def start(self):
        if self.fuel <= 0:
            raise LowFuelError

        if not self.started:
            self.started = True

    def move(self, distance):
        fuel_needs = distance * self.fuel_consumption
        if fuel_needs <= self.fuel:
            self.fuel -= fuel_needs
        else:
            raise NotEnoughFuel
