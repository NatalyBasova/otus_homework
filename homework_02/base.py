from abc import ABC


class Vehicle(ABC):

    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        pass

    def stop(self):
        pass

    def beep(self):
        print("Beep beep!")
