#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

# Adding parameters

from twilio.rest import Client
from pprint import pprint
from flight_search import FlightSearch



for n in range(0, len(sheet_data["prices"])):
    data = sheet_data["prices"][n]["iataCode"]
    if data == "":
        pass
    else:
        pass
