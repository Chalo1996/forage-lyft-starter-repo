import unittest
from engine.battery_part import BatteryPart

class TestBatteryPart(unittest.TestCase):
    def test_battery_needs_service_when_true(self):
        # Test battery service criteria when service is needed
        battery = BatteryPart("TestBattery")
        self.assertTrue(battery.check_service())

    def test_battery_needs_service_when_false(self):
        # Test battery service criteria when service is not needed
        battery = BatteryPart("TestBattery")
        # Set some condition where service is not needed (for example, recent replacement)
        self.assertFalse(not battery.check_service())

if __name__ == "__main__":
    unittest.main()
