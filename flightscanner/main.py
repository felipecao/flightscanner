from datetime import datetime

from dotenv import load_dotenv

from flightscanner.email_composer import EmailComposer
from flightscanner.email_service import EmailService
from flightscanner.kiwi_client import KiwiClient
from flightscanner.sheety_client import SheetyClient

load_dotenv()

MIN_NIGHTS = 13
MAX_NIGHTS = 28

EARLIEST_DEPARTURE = datetime(2024, 7, 9)
LATEST_DEPARTURE = datetime(2024, 8, 15)

sheety_client = SheetyClient()
kiwi_client = KiwiClient()
email_composer = EmailComposer()
email_service = EmailService()

trips = sheety_client.get_all_trips()

for trip in trips:
    cheapest_flights = kiwi_client.find_flights_below_max_price(
        origin=trip["origin"],
        destination=trip["destination"],
        max_price=trip["maxPrice"],
        earliest_departure=EARLIEST_DEPARTURE,
        latest_departure=LATEST_DEPARTURE,
        min_nights=MIN_NIGHTS,
        max_nights=MAX_NIGHTS,
    )

    email_contents = email_composer.write_table(cheapest_flights)
    # write_to_file("email.html", email_contents)

    email_service.send_email(
        f"Flights from {trip['origin']} to {trip['destination']}", email_contents
    )
