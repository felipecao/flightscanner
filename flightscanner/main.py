from datetime import datetime

from dotenv import load_dotenv

from flightscanner.email_composer import EmailComposer
from flightscanner.email_service import EmailService
from flightscanner.kiwi_client import KiwiClient
from flightscanner.sheety_client import SheetyClient

load_dotenv()


def to_datetime(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")


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
        earliest_departure=to_datetime(trip["earliestDeparture"]),
        latest_departure=to_datetime(trip["latestDeparture"]),
        min_nights=trip["minNights"],
        max_nights=trip["maxNights"],
    )

    email_contents = email_composer.write_table(cheapest_flights)
    recipients = trip["emails"]
    # write_to_file("email.html", email_contents)

    email_service.send_email(
        f"Flights from {trip['origin']} to {trip['destination']}", email_contents, recipients
    )
