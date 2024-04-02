import os

import requests


class SheetyClient:
    def __init__(self):
        self.SHEETY_AUTH = os.environ["SHEETY_AUTH"]

    def get_all_trips(self):
        endpoint = (
            "https://api.sheety.co/1552a9feb544663d2d6fd27739d9a5ee/buscaDeVoos/trips"
        )
        headers = {"Authorization": f"Bearer {self.SHEETY_AUTH}"}

        response = requests.get(url=endpoint, headers=headers)

        return response.json()["trips"]
