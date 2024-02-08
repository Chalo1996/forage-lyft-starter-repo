from abc import ABC, abstractmethod
from typing import List

class CarFactory(ABC):

    @abstractmethod
    def create_car(self):
        pass

    @staticmethod
    def check_tire_service_criteria(tire_wear_array: List[float]) -> bool:
        if any(wear >= 0.9 for wear in tire_wear_array):  # Carrigan tires
            return True
        elif sum(tire_wear_array) >= 3:  # Octoprime tires
            return True
        return False