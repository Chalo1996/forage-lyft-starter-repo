from cars.car import CarPart


class BatteryPart(CarPart):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        pass