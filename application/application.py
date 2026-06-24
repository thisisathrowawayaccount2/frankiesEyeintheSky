import time 
from collectors.base  import BaseCollector
from displays.base import BaseDisplay
from configurator.loader import Settings
from pipeline.flight_pipeline import FlightPipeline
from tracking.aircraft_tracker import AircraftTracker

class FlightApplication:
    """
    High-level coordinator for the application.
    """

    def __init__(
        self,
        collector: BaseCollector,
        pipeline: FlightPipeline,
        display: BaseDisplay,
        tracker: AircraftTracker,
        settings: Settings,
    ):
        self.collector = collector
        self.pipeline = pipeline
        self.display = display
        self.tracker = tracker
        self.settings = settings

    def run(self):
        
        while True:
            
            raw_aircraft = self.collector.collect()

            # update memory
            self.tracker.update(raw_aircraft)

            # get full state
            aircraft = self.tracker.all_aircraft()

            # process pipeline
            processed = self.pipeline.process(aircraft)

            # render
            for plane in processed:
                self.display.render(
                    plane
                )
            
            time.sleep(10)