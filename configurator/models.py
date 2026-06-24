from dataclasses import dataclass

@dataclass(frozen=True)
class HomeSettings:
    latitude: float
    longitude: float

@dataclass(frozen=True)
class TrackingSettings:
    max_distance: float
    refresh_seconds: int
    poll_interval: int

@dataclass(frozen=True)
class ScoringSettings:
    distance_weight: float
    altitude_weight: float

@dataclass(frozen=True)
class FavoriteSettings:
    airlines: list[str]

@dataclass(frozen=True)
class DisplaySettings:
    type: str
    max_aircraft: int

@dataclass(frozen=True)
class CollectorSettings:
    provider: str

@dataclass(frozen=True)
class Settings:
    home: HomeSettings
    tracking: TrackingSettings
    scoring: ScoringSettings
    favorites: FavoriteSettings
    collector: CollectorSettings
    display: DisplaySettings