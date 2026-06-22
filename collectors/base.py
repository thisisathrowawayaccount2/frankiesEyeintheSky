from abc import ABC, abstractmethod

from models.aircraft import Aircraft

class BaseCollector(ABC):
    """
    Defines the interface for all aircraft collectors.

    Every collector must implement get_aircraft().
    """

    @abstractmethod
    def get_aircraft(self) -> list[Aircraft]:
        """
        Returns a list of normalized Aircraft objects.
        """
        pass