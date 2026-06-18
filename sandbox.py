from models.aircraft import Aircraft

from pipeline.processor import process_aircraft

from collectors.dummy import DummyCollector

# plane = Aircraft(
#     hex_code="A1B2C3",
#     callsign="DAL1422",
#     latitude=27.95,
#     longitude=-82.45,
#     altitude_ft=34000,
#     speed_kts=485,
#     heading_deg=180,
#     vertical_rate_fpm=1200
# )

# print(plane)

collector = DummyCollector()

aircraft = collector.get_aircraft()

processed = process_aircraft(aircraft)

print(processed[0].score)