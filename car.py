from abc import ABC, abstractmethod
from .engine.engine_part import EnginePart
from .engine.battery_part import BatteryPart


class Car:
    def __init__(self, engine: EnginePart, battery: BatteryPart):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.check_service() or self.battery.check_service()