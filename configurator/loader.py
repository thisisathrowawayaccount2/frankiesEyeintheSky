from pathlib import Path
import yaml
from configurator.models import (
    FavoriteSettings,
    HomeSettings,
    ScoringSettings,
    Settings,
    TrackingSettings,
    DisplaySettings,
    ScoringSettings,
    CollectorSettings,
)

CONFIG_PATH = Path(__file__).parent / "settings.yaml"

def load_settings() -> Settings:
    """
    Load and validate application settings from YAML.
    """

    with CONFIG_PATH.open(
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
        collector=CollectorSettings(
            **data["collector"]
        ),
        display=DisplaySettings(
            **data["display"]
        ),
        scoring=ScoringSettings(
            **data["scoring"],
        ),
        favorites=FavoriteSettings(
            **data["favorites"],
        ),
    )