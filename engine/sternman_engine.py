from engine.engine import EnginePart

class SternmanEngine(EnginePart):

    def needs_service(self) -> bool:
        return self.warning_light