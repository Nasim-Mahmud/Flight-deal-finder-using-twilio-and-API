#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

# Adding parameters
import requests
from twilio.rest import Client
from pprint import pprint

sheety_headers = {
"Authorization": "Basic TmFzaW06MTk5NjIyODA="
}
sheety_parameters = {

}

sheety_response = requests.get(url="https://api.sheety.co/43bd6cbcf5d90c6b7ffb3c6b3c961f51/myFlightDeals/prices",
                        params=sheety_parameters, headers=sheety_headers)

sheety_data = sheety_response.json()
print(sheety_data["prices"])
