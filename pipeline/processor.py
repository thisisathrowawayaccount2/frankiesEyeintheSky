from models.aircraft import Aircraft
from scoring.ranking import score_aircraft

def process_aircraft(
        aircraft_list: list[Aircraft],
) -> list[Aircraft]:
    """
    Processes every aircraft through the pipeline.
    """

    for aircraft in aircraft_list:
        aircraft.score = score_aircraft(aircraft)
        aircraft = normalize_callsign(aircraft)

    return aircraft_list

def normalize_callsign(
        aircraft: Aircraft,
) -> Aircraft:
    aircraft.callsign = aircraft.callsign.strip()

    return aircraft