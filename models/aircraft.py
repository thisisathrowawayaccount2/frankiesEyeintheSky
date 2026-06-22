from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Aircraft:
    """
    Represents a normalized aircraft within the FlightBoard system.

    This model is independent of any API provider and serves as the canonical 
    representation of an aircraft throughout the application.
    """

    # Identity
    hex_code: str
    callsign: str

    # Telemetry
    latitude: float
    longitude: float
    altitude_ft: int
    speed_kts: float
    heading_deg: float
    vertical_rate_fpm: int = 0

    # Metadata
    aircraft_type: str = "Unknown"
    airline_code: str = "Unknown"
    airline_name: str = "Unknown"

    # Derived
    distance_miles: float = 0.0
    score: float = 0.0
    bearing_deg: float = 0.0
    heading_difference_deg: float = 0.0

    # Classifications
    is_military: bool = False
    is_private: bool = False
    is_cargo: bool = False

    # Display
    logo_path: Optional[str] = None

    # Time
    last_seen: datetime = field(default_factory=datetime.utcnow)