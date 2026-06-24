from abc import ABC, abstractmethod
from models.aircraft import Aircraft
from rules.engine import apply_rules
from scoring.features import distance_feature, altitude_feature
from configurator.loader import Settings

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

    def __init__(self, settings: Settings):
        self.settings = settings

    def score(
        self,
        aircraft: Aircraft,
    ) -> float:
        
        distance_score = distance_feature(
            aircraft.distance_miles
        )

        altitude_score = altitude_feature(
            aircraft.altitude_ft
        )

        base_score = (
            distance_score * self.settings.scoring.distance_weight
            + altitude_score * self.settings.scoring.altitude_weight
        )

        bonus = apply_rules(
            aircraft
        )

        return base_score + bonus