from datetime import datetime

from flightscanner.flight import CompleteFlight, RouteLeg


class EmailComposer:
    def __init__(self):
        self.DATE_FORMAT = "%d-%m-%Y HH:mm"

    def write_table(self, flights: list[CompleteFlight]) -> str:
        flights = self._sort_flights(flights)
        return self.TABLE_OPEN + "".join([self._write_one_row(f) for f in flights]) + self.TABLE_CLOSE

    @staticmethod
    def _sort_flights(flights: list[CompleteFlight]) -> list[CompleteFlight]:
        return sorted(
            flights, key=lambda flight: (len(flight.route), -flight.total_nights)
        )

    def _write_one_row(self, flight: CompleteFlight) -> str:
        return """
        <tr>
            <td>{origin_airport}</td>
            <td>{destination_airport}</td>
            <td>EUR {price}</td>
            <td>{total_nights}</td>
            <td>{routes}</td>
        </tr>
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

    TABLE_OPEN = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>Flight Information</title>
        <script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
        </head>
        <body>
        <h2>Flights</h2>
        <table class="sortable">
            <thead>
                <tr>
                    <th>Origin</th>
                    <th>Destination</th>
                    <th>Price</th>
                    <th>Number of Nights</th>
                    <th>Route</th>
                </tr>
            </thead>
            <tbody>
    """

    TABLE_CLOSE = """
            </tbody>
        </table>
        </body>
        </html>
    """
