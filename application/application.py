class FlightApplication:
    """
    High-level coordinator for the application.
    """

    def __init__(
        self,
        collector,
        pipeline,
        display,
    ):

        self.collector = collector
        self.pipeline = pipeline
        self.display = display

    def run(self):
        aircraft = self.collector.collect()

        ranked = self.pipeline.process(
            aircraft
        )

        for plane in ranked:
            self.display.render(
                plane
            )