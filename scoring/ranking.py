from models.aircraft import Aircraft
from scoring.features import altitude_feature, distance_feature
from config import ALTITUDE_WEIGHT, DISTANCE_WEIGHT
from scoring.strategy import DefaultScoringStrategy

_strategy = DefaultScoringStrategy()

def score_aircraft(
        aircraft,
) -> float:
    """
    Delegate scoring to the configured 
    scoring strategy.
    """

    return _strategy.score(
        aircraft
    )