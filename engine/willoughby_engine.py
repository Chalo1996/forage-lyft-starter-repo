from engine.engine import EnginePart


class WilloughbyEngine(EnginePart):
    def needs_service(self) -> bool:
        return self.mileage >= 60000