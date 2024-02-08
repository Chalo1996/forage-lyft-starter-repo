from battery.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine

class GlissadeCar:
    def __init__(self, engine: WilloughbyEngine, battery: SpindlerBattery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()