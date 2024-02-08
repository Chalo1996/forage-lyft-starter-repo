from engine.engine import EnginePart

class CapuletEngine(EnginePart):
    def needs_service(self) -> bool:
        return self.mileage >= 30000