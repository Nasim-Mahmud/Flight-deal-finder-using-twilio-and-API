# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

import requests

shetty_endpoint = "https://api.sheety.co/43bd6cbcf5d90c6b7ffb3c6b3c961f51/fd/prices"
tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"

tequila_apiKey_header = {
    "apikey": "mwtoLjx_0-VcKUyqwJBgOFr2omnjP88_"
}

shetty_response = requests.get(url=shetty_endpoint)
shetty_data = shetty_response.json()
print(shetty_data["prices"])

for names in shetty_data["prices"]:
    city_names = names["city"]
    prices = names["lowestPrice"]
    teq_parameters = {
        "term": city_names,
    }

    teq_response = requests.get(url=tequila_endpoint, params=teq_parameters, headers=tequila_apiKey_header)
    teq_data = teq_response.json()
    IATA_codes = teq_data["locations"][0]["code"]
    # print(IATA_codes)

    shetty_parameters = {
        "price": {
            "city": city_names,
            "iataCode": IATA_codes,
            "lowestPrice": prices
        }
    }
    shetty_put_endpoint = f"{shetty_endpoint}/1"
    IATA_shetty = requests.put(url=shetty_put_endpoint, json=shetty_parameters)
    print(IATA_shetty.text)
