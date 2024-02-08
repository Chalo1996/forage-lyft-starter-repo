import unittest
import battery.spindler_battery
from battery.nubbin_battery import NubbinBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_needs_service(self):
        spindler_battery = battery.spindler_battery.SpindlerBattery(last_service_date='2022-01-01')
        
        self.assertTrue(spindler_battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        spindler_battery = battery.spindler_battery.SpindlerBattery(last_service_date='2023-01-01')

        self.assertFalse(spindler_battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        nubbin_battery = NubbinBattery(last_service_date='2020-01-01')
        self.assertTrue(nubbin_battery.needs_service())

    def test_nubbin_battery_does_not_need_service(self):
        nubbin_battery = NubbinBattery(last_service_date='2023-01-01')
        self.assertFalse(nubbin_battery.needs_service())


if __name__ == '__main__':
    unittest.main()
