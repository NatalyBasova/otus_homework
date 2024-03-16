"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        self._engine = None

    @property
    def engine(self) -> Engine:
        return self._engine

    @engine.setter
    def engine(self, engine: Engine):
        if isinstance(engine, Engine):
            self._engine = engine
        else:
            raise TypeError

    def set_engine(self, engine: Engine):
        self.engine = engine
