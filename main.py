from configurator.loader import load_settings
from collectors.opensky_collector import OpenSkyCollector

#Temp
from collectors.dummy import DummyCollector

from displays.console import ConsoleDisplay
from application.application import FlightApplication
from pipeline.flight_pipeline import FlightPipeline

def main():
    
    #Load Config Settings First
    settings = load_settings()

    #Build Depenedencies
    collector = DummyCollector()
    display = ConsoleDisplay()

    #Build Pipeline (no global construction)
    pipeline = FlightPipeline(settings)

    #Create the Application
    app =  FlightApplication(
        collector=collector,
        pipeline=pipeline,
        display=display,
    )

    #Run the Application
    app.run()

if __name__ == "__main__":
    main()