from abc import ABC, abstractmethod
from models.aircraft import Aircraft
from config import DISTANCE_WEIGHT, ALTITUDE_WEIGHT
from rules.engine import apply_rules

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

        base_score = (
            distance * DISTANCE_WEIGHT
            + altitude * ALTITUDE_WEIGHT
        )

        bonus = apply_rules(
            aircraft
        )

        return base_score + bonus