from abc import ABC, abstractmethod

class CarPart(ABC):

    @abstractmethod
    def check_service(self) -> bool:
        pass