from models.aircraft import Aircraft

def favorite_airline_bonus(
    aircraft: Aircraft,
) -> float:
    """
    Return a bonus if the aircraft belongs
    to a preferred airline.
    """

    favorites = {}

    if aircraft.callsign.startswith(
        tuple(favorites)
    ):
        
        return 0.20
    
    return 0.0