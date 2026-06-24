from configurator.models import Settings
from models.aircraft import Aircraft
from scoring.strategy import DefaultScoringStrategy
from utils.geo import (
    haversine_distance,
    calculate_bearing,
    angular_difference,
)

class FlightPipeline:
    """
    Responsible for transforming, enriching,
    filtering, and scoring aircraft.
    """

    def __init__(self, settings: Settings,) -> None:
        self.settings = settings
        self.strategy = DefaultScoringStrategy(settings)

    def _normalize_callsign(
        self,
        aircraft: Aircraft,
    ) -> Aircraft:

        aircraft.callsign = aircraft.callsign.strip()

        return aircraft
    
    def _calculate_distance(
        self,
        aircraft: Aircraft
    ) -> Aircraft:
        
        aircraft.distance_miles = haversine_distance(
            self.settings.home.latitude,
            self.settings.home.longitude,
            aircraft.latitude,
            aircraft.longitude,
        )

        return aircraft
    
    def _determine_bearing(
        self,
        aircraft: Aircraft
    ) -> Aircraft:

        aircraft.bearing_deg = calculate_bearing(
            self.settings.home.latitude,
            self.settings.home.longitude,
            aircraft.latitude,
            aircraft.longitude
        )

        return aircraft
    
    def _calculate_heading_difference(
        self,
        aircraft: Aircraft,
    ) -> Aircraft:

        aircraft.heading_difference_deg = angular_difference(
            aircraft.heading_deg,
            aircraft.bearing_deg
        )
    
        return aircraft
    
    def _calculate_score(
        self,
        aircraft: Aircraft,
    ) -> Aircraft:

        aircraft.score = self.strategy.score(aircraft)

        return aircraft
    
    def _filter_by_distance(
        self,
        aircraft: Aircraft,
    ) -> Aircraft | None:

        if aircraft.distance_miles > self.settings.tracking.max_distance:
            return None
        
        return aircraft

    def process(
        self,
        aircraft_list: list[Aircraft],
    ) -> list[Aircraft]:

        """
        Exectue the complete enrichment pipeline ona  collection of 
        aircraft.

        Each aircraft is normalized, enriched with derived data,
        scored, filtered, and returned.
        """
        
        enriched: list[Aircraft] = []

        for aircraft in aircraft_list:
           aircraft = self._normalize_callsign(aircraft)
           aircraft = self._calculate_distance(aircraft)
           aircraft = self._determine_bearing(aircraft)
           aircraft = self._calculate_heading_difference(aircraft)
           aircraft = self._calculate_score(aircraft)
           aircraft = self._filter_by_distance(aircraft)
           if aircraft is None:
              continue
           enriched.append(aircraft)
        
        return enriched