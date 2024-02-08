from car_part import CarPart


class EnginePart(CarPart):
    def __init__(self, type: str):
        self.type = type

    def check_service(self) -> bool:
        # Custom logic for engine service criteria
        return True