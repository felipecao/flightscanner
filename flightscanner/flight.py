from dataclasses import dataclass


@dataclass
class Flight:
    origin: str
    destination: str
    price: str
    departure_time: str
    return_time: str
    airline_code: str

@dataclass
class RouteLeg:
    origin_airport: str
    destination_airport: str
    departure_at: str
    flight: str

@dataclass
class CompleteFlight:
    origin_airport: str
    destination_airport: str
    price: str
    total_nights: int
    departure_at: str
    route: list[RouteLeg]


