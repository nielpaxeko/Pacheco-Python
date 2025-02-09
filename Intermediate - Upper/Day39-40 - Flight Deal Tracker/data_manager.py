import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
SWEETY_ENDPOINT = os.getenv("SWEETY_ENDPOINT")



class DataManager:

    def __init__(self):
        self._user = os.environ["USERNAME"]
        self._password = os.environ["PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SWEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SWEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)