from models.aircraft import Aircraft
from scoring.features import altitude_feature, distance_feature

def score_aircraft(
        aircraft,
) -> float:
    """
    Compute the aircraft's overall relevance score.
    """

    distance = distance_feature(
        aircraft.distance_miles,
    )

    altitude = altitude_feature(
        aircraft.altitude.ft,
    )

    return (
        distance * 0.70
        + altitude * 0.30
    )