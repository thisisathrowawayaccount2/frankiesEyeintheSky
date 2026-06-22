from pathlib import Path
import yaml

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
        return yaml.safe_load(file)