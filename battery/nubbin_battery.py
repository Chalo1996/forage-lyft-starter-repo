import datetime
from battery import BatteryPart


class NubbinBattery(BatteryPart):

    def needs_service(self) -> bool:
        return (datetime.datetime.now() - self.last_service_date).days > 1460
