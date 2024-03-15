"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle


class Car(Vehicle):
    def __init__(self, engine):
        self.engine = engine

    def set_engine(engine):
        pass


# car1 = Car()
# car1.set_engine()
