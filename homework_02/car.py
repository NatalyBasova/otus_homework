"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle


class Car(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, engine):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(engine):
        pass


# car1 = Car()
# car1.set_engine()
