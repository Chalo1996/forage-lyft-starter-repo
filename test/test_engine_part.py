import unittest
from engine.engine_part import EnginePart

class TestEnginePart(unittest.TestCase):
    def test_engine_needs_service_when_true(self):
        # Test engine service criteria when service is needed
        engine = EnginePart("TestEngine")
        self.assertTrue(engine.check_service())

    def test_engine_needs_service_when_false(self):
        # Test engine service criteria when service is not needed
        engine = EnginePart("TestEngine")
        # Set some condition where service is not needed (for example, recent service)
        self.assertFalse(engine.check_service())

if __name__ == "__main__":
    unittest.main()
