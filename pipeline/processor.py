from models.aircraft import Aircraft
from scoring.ranking import score_aircraft
from pipeline.types import PipelineStage

from config import HOME_LATITUDE, HOME_LONGITUDE
from utils.geo import haversine_distance, calculate_bearing

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

def normalize_callsign(
    aircraft: Aircraft,
) -> Aircraft:
    
    aircraft.callsign = aircraft.callsign.strip()

    return aircraft

def calculate_score(
    aircraft: Aircraft,
) -> Aircraft:
    
    aircraft.score = score_aircraft(aircraft)

    return aircraft

PIPELINE: tuple[PipelineStage, ...] = (
    normalize_callsign,
    calculate_distance,
    determine_bearing,
    calculate_score,
) 

def process_aircraft(
    aircraft_list: list[Aircraft],
) -> list[Aircraft]:
    
    for aircraft in aircraft_list:
        for stage in PIPELINE:
            aircraft = stage(aircraft)
    
    return aircraft_list