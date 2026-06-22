from dataclasses import dataclass

@dataclass
class HomeSettings:
    latitude: float
    longitude: float

@dataclass
class TrackingSettings:
    max_distance: float

@dataclass
class ScoringSettings:
    distance_weight: float
    altitude_weight: float

@dataclass
class FavoriteSettings:
    airlines: list[str]

@dataclass
class Settings:
    home: HomeSettings
    tracking: TrackingSettings
    scoring: ScoringSettings
    favorites: FavoriteSettings