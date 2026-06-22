def distance_feature(
        distance_miles: float,
) -> float:
    """
    Convert distance into a normalized score.

    Closer aircraft receive larger values.
    """

    MAX_DISTANCE = 25.0

    score = 1 - min(distance_miles, MAX_DISTANCE) / MAX_DISTANCE

    return score

def altitude_feature(
        altitude_ft: float,
) -> float:
    """
    Lower aircraft are generally
    more interesting.
    """

    MAX_ALTITUDE = 40000

    score = 1 - min(
        altitude_ft,
        MAX_ALTITUDE,
    ) / MAX_ALTITUDE

    return score


