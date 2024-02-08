import unittest
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        capulet_engine = CapuletEngine(mileage=35000)
        self.assertTrue(capulet_engine.needs_service())

    def test_capulet_engine_does_not_need_service(self):
        capulet_engine = CapuletEngine(mileage=20000)
        self.assertFalse(capulet_engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_needs_service(self):
        willoughby_engine = WilloughbyEngine(mileage=70000)
        self.assertTrue(willoughby_engine.needs_service())

    def test_willoughby_engine_does_not_need_service(self):
        willoughby_engine = WilloughbyEngine(mileage=50000)
        self.assertFalse(willoughby_engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_sternman_engine_needs_service(self):
        sternman_engine = SternmanEngine(warning_light=True)
        self.assertTrue(sternman_engine.needs_service())

    def test_sternman_engine_does_not_need_service(self):
        sternman_engine = SternmanEngine(warning_light=False)
        self.assertFalse(sternman_engine.needs_service())

if __name__ == '__main__':
    unittest.main()
