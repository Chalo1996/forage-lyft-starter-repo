from cars.car import CarPart


class EnginePart(CarPart):
    def __init__(self, mileage: int, warning_light: bool = False):
        self.mileage = mileage
        self.warning_light = warning_light

    def needs_service(self) -> bool:
        pass