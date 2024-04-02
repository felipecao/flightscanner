from datetime import date, timedelta, datetime

from dotenv import load_dotenv

from flightscanner.kiwi_client import KiwiClient
from sheety_client import SheetyClient

load_dotenv()

TOMORROW = date.today() + timedelta(days=1)
SIX_MONTHS_FROM_NOW = date.today() + timedelta(days=6 * 30)
MIN_NIGHTS = 13
MAX_NIGHTS = 28

EARLIEST_DEPARTURE = datetime(2024, 7, 9)
LATEST_DEPARTURE = datetime(2024, 8, 15)

sheety_client = SheetyClient()
kiwi_client = KiwiClient()

trips = sheety_client.get_all_trips()

for trip in trips:
    cheapest_flights = kiwi_client.find_first_flight_below_max_price(
        origin=trip['origin'],
        destination=trip['destination'],
        max_price=trip['maxPrice'],
        earliest_departure=EARLIEST_DEPARTURE,
        latest_departure=LATEST_DEPARTURE,
        min_nights=MIN_NIGHTS,
        max_nights=MAX_NIGHTS
    )
