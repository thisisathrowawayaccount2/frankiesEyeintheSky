from dataclasses import dataclass
from datetime import datetime

@dataclass
class Aircraft:
    hex_code: str

    callsign: str

    airline_code: str
    airline_name: str

    aircraft_type: str
    aircraft_name: str

    latitude: float
    longitude: float

    altitude_ft: int
    speed_kts: int
    heading: int

    distance_miles: float

    is_military: bool = False
    is_private: bool = False
    is_cargo: bool = False

    origin: str | None = None
    destination: str | None = None

    logo_path: str | None = None

    last_seen: datetime | None = None