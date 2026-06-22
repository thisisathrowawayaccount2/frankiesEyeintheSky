from models.aircraft import Aircraft
from rules.airlines import favorite_airline_bonus

def apply_rules(
    aircraft: Aircraft,
) -> float:
    """
    Compute all business rule bonuses.
    """

    bonus = 0.0

    bonus += favorite_airline_bonus(
        aircraft
    )

    return bonus