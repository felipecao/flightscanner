import os

import requests

from flight import RouteLeg, CompleteFlight


class KiwiClient:
    def __init__(self):
        self.API_KEY = os.environ["KIWI_API_KEY"]
        self.DATE_FORMAT = "%d/%m/%Y"

    def find_flights_below_max_price(
        self,
        origin,
        destination,
        max_price,
        earliest_departure,
        latest_departure,
        min_nights,
        max_nights,
    ) -> list[CompleteFlight]:
        endpoint = "https://api.tequila.kiwi.com/v2/search"
        headers = {"apikey": self.API_KEY}
        parameters = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": earliest_departure.strftime(self.DATE_FORMAT),
            "date_to": latest_departure.strftime(self.DATE_FORMAT),
            "nights_in_dst_from": min_nights,
            "nights_in_dst_to": max_nights,
            "price_to": max_price,
            "selected_cabins": "M",  # M = economy
            "curr": "EUR",
        }

        response = requests.get(url=endpoint, headers=headers, params=parameters).json()
        flights = response["data"]

        return [self._map_complete_flight(x) for x in flights]

    @staticmethod
    def _map_complete_flight(entry):
        routes = []

        for r in entry["route"]:
            routes.append(
                RouteLeg(
                    origin_airport=r["flyFrom"],
                    destination_airport=r["flyTo"],
                    departure_at=r["local_departure"],
                    flight=r["airline"] + str(r["flight_no"]),
                )
            )

        return CompleteFlight(
            origin_airport=entry["flyFrom"],
            destination_airport=entry["flyTo"],
            price=entry["price"],
            total_nights=entry["nightsInDest"],
            departure_at=entry["local_departure"],
            route=routes,
        )
