from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery

class CalliopeCar:
    def __init__(self, engine: CapuletEngine, battery: SpindlerBattery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()