from displays.base import BaseDisplay
from models.aircraft import Aircraft

class ConsoleDisplay(
    BaseDisplay,
): 
    def render(
        self,
        aircraft: Aircraft,
    ) -> None:
        print()

        print("=" * 40)

        print(
            aircraft.callsign
        )

        print(
            f"Distance: {aircraft.distance_miles:.1f} mi"
        )

        print(
            f"Altitude: {aircraft.altitude_ft:,.0f} ft"
        )

        print(
            f"Score: {aircraft.score:.2f}"
        )

        print("=" * 40)