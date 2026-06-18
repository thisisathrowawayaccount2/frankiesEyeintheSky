from models.aircraft import Aircraft
from collectors.base import BaseCollector

class DummyCollector(BaseCollector):

    def get_aircraft(self) -> list[Aircraft]:
        return [
            Aircraft(
                hex_code="ABC123",
                callsign="DAL1422",
                latitude=27.95,
                longitude=-82.45,
                altitude_ft=34000,
                speed_kts=480,
                heading_deg=180,
                airline_code="DAL",
                airline_name="Delta Air Lines",
                aircraft_type="A321",
            )
        ]