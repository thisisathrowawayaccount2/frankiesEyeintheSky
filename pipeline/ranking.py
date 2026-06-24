from models.aircraft import Aircraft

def rank_aircraft(
    aircraft_list: list[Aircraft],
) -> list[Aircraft]:

    return sorted(
        aircraft_list,
        key=lambda aircraft: aircraft.score,
        reverse=True,
    )