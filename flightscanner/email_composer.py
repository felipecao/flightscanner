from datetime import datetime

from flightscanner.flight import CompleteFlight, RouteLeg


class EmailComposer:
    def __init__(self):
        self.DATE_FORMAT = "%d-%m-%Y HH:mm"

    def write_table(self, flights: list[CompleteFlight]) -> str:
        flights = self._sort_flights(flights)
        return "".join([self._write_one_table(f) for f in flights])

    @staticmethod
    def _sort_flights(flights: list[CompleteFlight]) -> list[CompleteFlight]:
        return sorted(
            flights, key=lambda flight: (len(flight.route), -flight.total_nights)
        )

    def _write_one_table(self, flight: CompleteFlight) -> str:
        return """
        <table border="1px solid black" style="border-collapse: collapse">
            <tr>
                <td><strong>Origin: </strong></td>
                <td>{origin_airport}</td>
                <td><strong>Destination: </strong></td>
                <td>{destination_airport}</td>
                <td><strong>Price: </strong></td>
                <td>{price}</td>
                <td><strong>Nights: </strong></td>
                <td>{total_nights}</td>
            </tr>
            <tr>
                <td colspan="8">
                    {routes}
                </td>
            </tr>
        </table>
        <br/>
        """.format(
            origin_airport=flight.origin_airport,
            destination_airport=flight.destination_airport,
            price=flight.price,
            total_nights=flight.total_nights,
            routes=self._write_routes_cell(flight.route),
        )

    def _write_routes_cell(self, route: list[RouteLeg]) -> str:
        text = "<strong>Route: </strong><br/>"

        for r in route:
            text += f"{r.origin_airport} > {r.destination_airport} | flight {r.flight} | departure: {self._convert_datetime(r.departure_at)} | <br/>"

        return text

    @staticmethod
    def _convert_datetime(input_datetime_str, output_format="%d-%m-%Y %H:%M"):
        input_format = "%Y-%m-%dT%H:%M:%S.%fZ"

        # Parse input datetime string
        input_datetime = datetime.strptime(input_datetime_str, input_format)

        # Format datetime according to output format
        output_datetime_str = input_datetime.strftime(output_format)

        return output_datetime_str
