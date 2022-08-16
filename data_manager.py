import requests

SHEETY_ENDPOINT = "https://api.sheety.co/43bd6cbcf5d90c6b7ffb3c6b3c961f51/myFlightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination = {}

    def getting_destination:
        sheety_response = requests.get(url=SHEETY_ENDPOINT)
