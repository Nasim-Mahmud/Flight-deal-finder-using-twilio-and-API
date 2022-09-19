# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

import requests

shetty_endpoint = "https://api.sheety.co/43bd6cbcf5d90c6b7ffb3c6b3c961f51/fd/prices"
tequila_endpoint = "https://api.tequila.kiwi.com/v2/search"

tequila_apiKey_header = {
    "apikey": "mwtoLjx_0-VcKUyqwJBgOFr2omnjP88_"
}

teq_parameters = {
    "fly_from": "FRA"
}

response = requests.get(url=tequila_endpoint, params=teq_parameters, headers=tequila_apiKey_header)
print(response.text)