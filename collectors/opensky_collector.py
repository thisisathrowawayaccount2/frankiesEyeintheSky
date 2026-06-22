import requests
from typing import List, Optional
from collectors.base import BaseCollector
from models.aircraft import Aircraft

class OpenSkyCollector(BaseCollector):
    """
    Collects aircraft data from OpenSky Network API and normalizes
    it into Aircraft objects.
    """
    BASE_URL = "https://opensky-network.org/api/states/all"
    
    def _parse_state(self, state: list) -> Optional[Aircraft]:
        try:
            return Aircraft(
                hex_code=state[0].strip() if state[0] else "UNKNOWN",
                callsign=(state[1] or "UNKNOWN").strip(),
                longitude=state[5] or 0.0,
                latitude=state[6] or 0.0,
                altitude_ft=int(state[7] or 0),
                speed_kts=float(state[9] or 0.0),
                heading_deg=float(state[10] or 0.0),

                #derived fields still default here
            )

        except Exception:
            return None


    def collect(self) -> list[Aircraft]:
        response = requests.get(self.BASE_URL, timeout=10)

        if response.status_code != 200:
            return []

        data = response.json()

        states = data.get("states", [])

        aircraft_list: list[Aircraft] = []

        for raw_state in states:
            aircraft = self._parse_state(raw_state)
            if aircraft:
                aircraft_list.append(aircraft)
        
        return aircraft_list
