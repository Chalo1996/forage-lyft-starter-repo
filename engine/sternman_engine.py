from car import Car
from car_factory import CarFactory
from .engine_part import EnginePart
from .battery_part import BatteryPart


class SternmanCarFactory(CarFactory):
    def create_car(self):
        engine = EnginePart("SternmanEngine")
        battery = BatteryPart("SternmanBattery")
        return Car(engine, battery)