from car import Car
from car_factory import CarFactory
from .engine_part import EnginePart
from .battery_part import BatteryPart


class WilloughbyCarFactory(CarFactory):
    def create_car(self):
        engine = EnginePart("WilloughbyEngine")
        battery = BatteryPart("WilloughbyBattery")
        return Car(engine, battery)