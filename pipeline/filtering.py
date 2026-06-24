from models.aircraft import Aircraft

def filter_distance(
    aircraft_list: list[Aircraft],
    max_distance: float,
) -> list[Aircraft]:

    return [
        aircraft
        for aircraft in aircraft_list
        if aircraft.distance_miles <= max_distance
    ]