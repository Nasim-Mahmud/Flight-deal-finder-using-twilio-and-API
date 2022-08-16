#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

# Adding parameters
import requests
from twilio.rest import Client
from pprint import pprint
from flight_search import FlightSearch

sheety_headers = {
"Authorization": "Basic TmFzaW06MTk5NjIyODA="
}
sheety_parameters = {

}

sheet_data = sheety_response.json()

for n in range(0, len(sheet_data["prices"])):
    data = sheet_data["prices"][n]["iataCode"]
    if data == "":
        pass
    else:
        pass
