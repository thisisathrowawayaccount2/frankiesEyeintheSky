from models.aircraft import Aircraft

def score_aircraft(aircraft: Aircraft) -> float:
    """
    Calculates an interest score for a given aircraft.

    The higher the score the more interesting the aircraft.
    """
    
    score = 100

    score -= aircraft.distance_miles * 10

    score -= aircraft.altitude_ft / 1000

    if aircraft.is_military:
        score += 100

    if aircraft.is_private:
        score += 50
    
    if aircraft.is_cargo:
        score += 20

    return score