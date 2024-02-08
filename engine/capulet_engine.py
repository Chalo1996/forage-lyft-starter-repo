from car import Car
from car_factory import CarFactory
from .engine_part import EnginePart
from .battery_part import BatteryPart


class CapuletCarFactory(CarFactory):
    def create_car(self):
        engine = EnginePart("CapuletEngine")
        battery = BatteryPart("CapuletBattery")
        return Car(engine, battery)
    
    def needs_service(self):
        return True