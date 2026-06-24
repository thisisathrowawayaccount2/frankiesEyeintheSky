from models.aircraft import Aircraft

class AircraftTracker:
    """
    Maintains aircraft state across multipe
    collection cycles.
    """

    def __init__(self) -> None:
        
        self._aircraft: dict[str, Aircraft] = {}

    def update(
        self,
        aircraft: list[Aircraft]
    ) -> None:
        for plane in aircraft:
            self._aircraft[plane.hex_code] = plane

    def all_aircraft(self) -> list[Aircraft]:
        return list(self._aircraft.values())