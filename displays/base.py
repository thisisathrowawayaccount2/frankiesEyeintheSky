from abc import ABC
from abc import abstractmethod
from models.aircraft import Aircraft

class BaseDisplay(ABC):
    """
    Base Class for all application displays.
    """

    @abstractmethod
    def render(
        self,
        aircraft: Aircraft,
    ) -> None:
        """
        Render one aircraft
        """

        raise NotImplementedError
    