import os
from flight import Flight
from twilio.rest import Client


class TwilioClient:

    def __init__(self):
        self.ACCOUNT_ID = os.environ['TWILIO_ACCOUNT_SID']
        self.AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
        self.PRINT_ONLY = True

    def send_sms_notification(self, cheapest_flight: Flight):
        client = Client(self.ACCOUNT_ID, self.AUTH_TOKEN)
        body = self.__format_text__(cheapest_flight)

        if self.PRINT_ONLY:
            print(body)
            return

        client.messages.create(
            from_='+16592243829',
            body=body,
            to='+5522988752737'
        )

    @staticmethod
    def __format_text__(cheapest_flight: Flight):
        return (f"Cheap flight alert! {cheapest_flight.price} "
                f"from {cheapest_flight.origin} to {cheapest_flight.destination}, "
                f"flying {cheapest_flight.airline_code} from date {cheapest_flight.departure_time} "
                f"to {cheapest_flight.return_time}")
