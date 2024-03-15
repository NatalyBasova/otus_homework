"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, engine, cargo, max_cargo):
        super().__init__(weight, fuel, fuel_consumption, engine)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        if weight + self.cargo <= self.max_cargo:
            self.cargo += weight
        else:
            raise CargoOverload
