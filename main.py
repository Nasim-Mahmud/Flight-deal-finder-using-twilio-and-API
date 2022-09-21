# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

import requests
import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta

sheety_endpoint = "https://api.sheety.co/43bd6cbcf5d90c6b7ffb3c6b3c961f51/fd/prices"
tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"

tequila_apiKey_header = {
    "apikey": "mwtoLjx_0-VcKUyqwJBgOFr2omnjP88_"
}

sheety_response = requests.get(url=sheety_endpoint)
sheety_data = sheety_response.json()

# Putting the IATA codes into the Google sheets using tequila and sheety api
# for i in range(0, len(sheety_data["prices"])):
#     city_names = sheety_data["prices"][i]["city"]
#     prices = sheety_data["prices"][i]["lowestPrice"]
#     teq_parameters = {
#         "term": city_names,
#     }
#
#     teq_response = requests.get(url=tequila_endpoint, params=teq_parameters, headers=tequila_apiKey_header)
#     teq_data = teq_response.json()
#     IATA_codes = teq_data["locations"][0]["code"]
#
#     sheety_parameters = {
#         "price": {
#             "iataCode": IATA_codes,
#         }
#     }
#
#     sheety_put_endpoint = f"{sheety_endpoint}/{i + 2}"
#     IATA_sheety = requests.put(url=sheety_put_endpoint, json=sheety_parameters)

#     Cheapest flight search
teq_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
today_date = datetime.strftime(datetime.now(), "%d/%m/%Y")
target_date = datetime.strftime(datetime.now() + relativedelta(days = +1), "%d/%m/%Y")
print(today_date)
print(target_date)

# for i in range(0, len(sheety_data["prices"])):
iataCodes = sheety_data["prices"][0]["iataCode"]
teq_parameters = {
    "fly_from": "LHR",
    "fly_to": "IST",
    "date_from": today_date,
    "date_to": target_date,
    "curr": "USD"


}

teq_response = requests.get(url=teq_search_endpoint, params=teq_parameters, headers=tequila_apiKey_header)
teq_data = teq_response.json()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(teq_data["data"])
