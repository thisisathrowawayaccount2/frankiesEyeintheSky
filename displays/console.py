def show(aircraft):

    print()
    print('=' * 40)

    print(f"{aircraft.airline_name}")
    print(f"{aircraft.callsign}")

    print()

    print(aircraft.aircraft_name)

    print()

    print(f"{aircraft.altitude_ft:,} ft")
    print(f"{aircraft.speed_kts} kts")
    print(f"{aircraft.distance_miles:.1f} mi")

    print("=" * 40)