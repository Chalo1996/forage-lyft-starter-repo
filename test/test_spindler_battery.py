import unittest
from datetime import datetime, timedelta
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_needs_service_within_two_years(self):
        last_service_date = datetime.now() - timedelta(days=365) * 2
        spindler_battery = SpindlerBattery(last_service_date=last_service_date)

        self.assertTrue(spindler_battery.needs_service())

    def test_spindler_battery_does_not_need_service_within_three_years(self):
        last_service_date = datetime.now() - timedelta(days=365) * 3
        spindler_battery = SpindlerBattery(last_service_date=last_service_date)

        self.assertFalse(spindler_battery.needs_service())

if __name__ == '__main__':
    unittest.main()
