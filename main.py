while True:
    aircraft = collector.get_aircraft()

    ranked = sorted(
        aircraft,
        key=score_aircraft,
        reverse=True
    )

    displays.console.show(
        ranked[0]
    )

    sleep(10)