from deprecated import deprecated

import requests
import os


class SheetyClient:
    def __init__(self):
        self.SHEETY_AUTH = os.environ['SHEETY_AUTH']

    def get_all_trips(self):
        endpoint = 'https://api.sheety.co/1552a9feb544663d2d6fd27739d9a5ee/buscaDeVoos/trips'
        headers = {
            'Authorization': f"Bearer {self.SHEETY_AUTH}"
        }

        response = requests.get(url=endpoint, headers=headers)

        return response.json()['trips']

    @deprecated
    def get_all_destinations(self):
        endpoint = 'https://api.sheety.co/1552a9feb544663d2d6fd27739d9a5ee/flightDeals/prices'
        headers = {
            'Authorization': f"Bearer {self.SHEETY_AUTH}"
        }

        response = requests.get(url=endpoint, headers=headers)

        return response.json()['prices']

    @deprecated
    def add_new_customer(self, first_name, last_name, email):
        endpoint = 'https://api.sheety.co/1552a9feb544663d2d6fd27739d9a5ee/flightDeals/users'
        headers = {
            'Authorization': f"Bearer {self.SHEETY_AUTH}"
        }
        body = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email,
            }
        }

        response = requests.post(url=endpoint, headers=headers, json=body)

        return response

    def get_all_customers(self):
        endpoint = 'https://api.sheety.co/1552a9feb544663d2d6fd27739d9a5ee/flightDeals/users'
        headers = {
            'Authorization': f"Bearer {self.SHEETY_AUTH}"
        }

        response = requests.get(url=endpoint, headers=headers)

        return response.json()['users']