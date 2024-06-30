from dataclasses import dataclass


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
    price: int
    total_nights: int
    departure_at: str
    route: list[RouteLeg]
