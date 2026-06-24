from models.aircraft import Aircraft
from scoring.features import altitude_feature, distance_feature
from scoring.strategy import ScoringStrategy

def score_aircraft(
        aircraft: Aircraft,
        strategy: ScoringStrategy,
) -> float:
    """
    Delegate scoring to the configured 
    scoring strategy.
    """

    return _strategy.score(
        aircraft
    )