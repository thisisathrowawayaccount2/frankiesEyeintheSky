from models.aircraft import Aircraft
from scoring.ranking import score_aircraft
from pipeline.types import PipelineStage
from configurator.loader import load_settings
from utils.geo import haversine_distance, calculate_bearing, angular_difference

def filter_by_distance(aircraft: Aircraft) -> Aircraft | None:
    if aircraft.distance_miles > max_distance:
        return None
    return aircraft

def calculate_distance(
        aircraft: Aircraft,
) -> Aircraft:
    """
    Calculates the distance from the user's home
    to the aircraft
    """

    aircraft.distance_miles = haversine_distance(
        HOME_LATITUDE,
        HOME_LONGITUDE,
        aircraft.latitude,
        aircraft.longitude,
    )

    return aircraft

def determine_bearing(
    aircraft: Aircraft,
) -> Aircraft:
    """
    Determine the compass bearing from the
    observer to the aircraft.
    """

    aircraft.bearing_deg = calculate_bearing(
        HOME_LATITUDE,
        HOME_LONGITUDE,
        aircraft.latitude,
        aircraft.longitude,
    )

    return aircraft

def calculate_heading_difference(
        aircraft: Aircraft,
) -> Aircraft:
    """
    Compare aircraft heading with the bearing
    from the observer.
    """

    aircraft.heading_difference_deg = angular_difference(
        aircraft.heading_deg,
        aircraft.bearing_deg,
    )

    return aircraft

def normalize_callsign(
    aircraft: Aircraft,
) -> Aircraft:
    
    aircraft.callsign = aircraft.callsign.strip()

    return aircraft

def calculate_score(
    aircraft: Aircraft,
) -> Aircraft:
    
    aircraft.score = score_aircraft(aircraft, strategy,)

    return aircraft

def process_aircraft(
    aircraft_list: list[Aircraft],
) -> list[Aircraft]:

    enriched: list[Aircraft] = []
    
    for aircraft in aircraft_list:
        for stage in PIPELINE:
            aircraft = stage(aircraft)
        enriched.append(aircraft)
    
    return enriched