from configurator.loader import load_settings
from collectors.opensky_collector import OpenSkyCollector

#Temp
from collectors.dummy import DummyCollector

from displays.console import ConsoleDisplay
from application.application import FlightApplication
from pipeline.flight_pipeline import FlightPipeline
from tracking.aircraft_tracker import AircraftTracker

def main():
    
    #Load Config Settings First
    settings = load_settings()

    #Build Depenedencies
    collector = DummyCollector()
    display = ConsoleDisplay()
    tracker = AircraftTracker()

    #Build Pipeline (no global construction)
    pipeline = FlightPipeline(settings)

    #Create the Application
    app =  FlightApplication(
        collector=collector,
        pipeline=pipeline,
        display=display,
        tracker=tracker,
        settings=settings,
    )

    #Run the Application
    app.run()

if __name__ == "__main__":
    main()