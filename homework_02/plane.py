"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(
        self,
        weight: int = 0,
        fuel: int = 0,
        fuel_consumption: int = 0,
        max_cargo: int = 0,
    ):
        super().__init__(weight, fuel, fuel_consumption)

        self.max_cargo = max_cargo
        self.cargo = 0

    # def load_cargo(self, weight):
    #     if weight + self.cargo <= self.max_cargo:
    #         self.cargo += weight
    #     else:
    #         raise CargoOverload
