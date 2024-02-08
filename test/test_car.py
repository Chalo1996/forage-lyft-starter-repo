import unittest

from car import Car
from car_part import CarPart
from car_factory import CarFactory
from engine.engine_part import EnginePart
from engine.battery_part import BatteryPart
from engine.capulet_engine import CapuletCarFactory
from engine.sternman_engine import SternmanCarFactory
from engine.willoughby_engine import WilloughbyCarFactory


class TestCar(unittest.TestCase):
    def test_engine_needs_service(self):
        # Test engine service criteria
        engine = EnginePart("TestEngine")
        engine_needs_service = engine.check_service()
        self.assertFalse(engine_needs_service)

    def test_battery_needs_service(self):
        # Test battery service criteria
        battery = BatteryPart("TestBattery")
        battery_needs_service = battery.check_service()
        self.assertFalse(battery_needs_service)

    def test_car_needs_service(self):
        # Test car service criteria
        capulet_factory = CapuletCarFactory()
        capulet_car = capulet_factory.create_car()
        self.assertFalse(capulet_car.needs_service())

        sternman_factory = SternmanCarFactory()
        sternman_car = sternman_factory.create_car()
        self.assertFalse(sternman_car.needs_service())

        willoughby_factory = WilloughbyCarFactory()
        willoughby_car = willoughby_factory.create_car()
        self.assertFalse(willoughby_car.needs_service())


if __name__ == "__main__":
    unittest.main()
