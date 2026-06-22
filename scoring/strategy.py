from abc import ABC, abstractmethod
from models.aircraft import Aircraft
from config import DISTANCE_WEIGHT, ALTITUDE_WEIGHT

class ScoringStrategy(ABC):
    """
    Base class for all aircraft scoring strategies.
    """

    @abstractmethod
    def score(
        self,
        aircraft: Aircraft,
    ) -> float:
        """
        Compute a score for an aircraft.
        """

        raise NotImplementedError

class DefaultScoringStrategy(
    ScoringStrategy,
):
    """
    Default scoring algorithm.
    """

    def score(
        self,
        aircraft: Aircraft,
    ) -> float:
        
        distance = distance.feature(
            aircraft.distance_miles
        )

        altitude = altitude.feature(
            aircraft.altitude_ft
        )

        return (
            distance * DISTANCE_WEIGHT
            + altitude * ALTITUDE_WEIGHT
        )