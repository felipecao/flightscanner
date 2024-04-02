from datetime import date, timedelta
from sheety_client import SheetyClient
from kiwi_client import KiwiClient
from email_service import EmailService
from flight import Flight


def format_email_text(cheapest_flight: Flight):
    return (f"Cheap flight alert! {cheapest_flight.price} "
            f"from {cheapest_flight.origin} to {cheapest_flight.destination}, "
            f"flying {cheapest_flight.airline_code} from date {cheapest_flight.departure_time} "
            f"to {cheapest_flight.return_time}")


sheety_client = SheetyClient()
kiwi_client = KiwiClient()
email_service = EmailService()

DEPARTURE_AIRPORT = 'BCN'
TOMORROW = date.today() + timedelta(days=1)
SIX_MONTHS_FROM_NOW = date.today() + timedelta(days=6 * 30)
MIN_NIGHTS = 7
MAX_NIGHTS = 28

destinations = sheety_client.get_all_destinations()
users = sheety_client.get_all_customers()

for dst in destinations:
    print(f"Searching flights from {DEPARTURE_AIRPORT} to {dst['iataCode']}...")
    cheapest_flight = kiwi_client.find_first_flight_below_max_price(DEPARTURE_AIRPORT, dst['iataCode'], dst['lowestPrice'], TOMORROW,
                                                                    SIX_MONTHS_FROM_NOW, MIN_NIGHTS, MAX_NIGHTS)

    if cheapest_flight is not None:
        for user in users:
            email_subject = 'Cheap flight alert!'
            email_body = format_email_text(cheapest_flight)
            email_service.send_email(user['email'], email_subject, email_body)
