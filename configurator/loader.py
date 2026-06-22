from pathlib import Path
import yaml
from configurator.models import (
    FavoriteSettings,
    HomeSettings,
    ScoringSettings,
    Settings,
    TrackingSettings,
)

CONFIG_PATH = (
    Path(__file__)
    .parent
    / "settings.yaml"
)

def load_settings() -> dict:
    """
    Load app settings from YAML.
    """

    with open(
        CONFIG_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        data = yaml.safe_load(file)
    
    return Settings(
        home=HomeSettings(
            **data["home"],
        ),
        tracking=TrackingSettings(
            **data["tracking"],
        ),
        scoring=ScoringSettings(
            **data["scoring"],
        ),
        favorites=FavoriteSettings(
            **data["favorites"],
        ),
    )