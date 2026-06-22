from collectors.dummy import DummyCollector
from displays.base import ConsoleDisplay
from scoring.strategy import DefaultScoringStrategy

def main():
    settings = load_settings()

    collector = DummyCollector()

    display = ConsoleDisplay()

    strategy = DefaultScoringStrategy(settings)

    pipeline = FlightPipeline(
        collector=collector,
        strategy=strategy,
        display=display,
    )

    pipeline.run()

if __name__ == "__main__":
    main()