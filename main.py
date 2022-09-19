# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

import requests

shetty_endpoint = "https://api.sheety.co/43bd6cbcf5d90c6b7ffb3c6b3c961f51/fd/prices"
tequila_endpoint = "https://api.tequila.kiwi.com/v2/search"

tequila_apiKey = "mwtoLjx_0-VcKUyqwJBgOFr2omnjP88_"

teq_parameters = {
    "apikey": tequila_apiKey,
    "fly_from": "Dhaka"
}

res