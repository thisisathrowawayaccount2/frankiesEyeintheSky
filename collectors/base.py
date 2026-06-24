from abc import ABC, abstractmethod
from models.aircraft import Aircraft

class BaseCollector(ABC):
    """
    Defines the interface for all aircraft collectors.

    Every collector must implement collect().
    """

    @abstractmethod
    def collect(self) -> list[Aircraft]:
        """
        Returns a list of normalized Aircraft objects.
        """
        pass