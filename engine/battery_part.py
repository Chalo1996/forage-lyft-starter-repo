from car_part import CarPart


class BatteryPart(CarPart):
    def __init__(self, type: str):
        self.type = type

    def check_service(self) -> bool:
        # Custom logic for battery service criteria
        return True