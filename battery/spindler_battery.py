from datetime import datetime
from battery import BatteryPart


class SpindlerBattery(BatteryPart):
    def needs_service(self) -> bool:
        return (datetime.now() - self.last_service_date).days > 365 * 3