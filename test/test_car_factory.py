import unittest
z cars.car_factory import CarFactory

class TestCarFactory(unittest.TestCase):
    def test_carrigan_tire_needs_service(self):
        tire_wear_array = [0.8, 0.95, 0.7, 0.85]
        self.assertTrue(CarFactory.check_tire_service_criteria(tire_wear_array))

    def test_carrigan_tire_does_not_need_service(self):
        tire_wear_array = [0.8, 0.85, 0.7, 0.8]
        self.assertFalse(CarFactory.check_tire_service_criteria(tire_wear_array))

    def test_octoprime_tire_needs_service(self):
        tire_wear_array = [0.9, 1.0, 0.8, 1.0]
        self.assertTrue(CarFactory.check_tire_service_criteria(tire_wear_array))

    def test_octoprime_tire_does_not_need_service(self):
        tire_wear_array = [0.8, 0.85, 0.7, 0.85]
        self.assertFalse(CarFactory.check_tire_service_criteria(tire_wear_array))

if __name__ == '__main__':
    unittest.main()
