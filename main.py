# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
import requests
import pprint
import smtplib
from datetime import datetime
from dateutil.relativedelta import relativedelta

sheety_prices_endpoint = "https://api.sheety.co/75f004290b7a8e66b7e5741a6a9e4137/fdV10/prices"
sheety_users_endpoint = "https://api.sheety.co/75f004290b7a8e66b7e5741a6a9e4137/fdV10/users"
tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"

my_email = "tmailtwo02@yahoo.com"
my_pass = "txrlccemnhpedcvj"

till_days = 30

tequila_apiKey_header = {
    "apikey": "mwtoLjx_0-VcKUyqwJBgOFr2omnjP88_"
}

sheety_response = requests.get(url=sheety_prices_endpoint)
sheety_data = sheety_response.json()


# TODO: Putting the IATA codes into the Google sheets using tequila and sheety api. Once used, comment out these codes

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
#     sheety_put_endpoint = f"{sheety_prices_endpoint}/{i + 2}"
#     IATA_sheety = requests.put(url=sheety_put_endpoint, json=sheety_parameters)

# TODO: Sending the offer notification to the user via email
def user_details():
    firstName = input("What is your first name?\n").title()
    lastName = input("What is your last name?\n").title()
    # Haven't added mail verification yet.
    userMailId = input("What is your email?\n")
    checkingUserMailId = input("Type your mail again.\n")

    if userMailId == checkingUserMailId:
        sheety_user_parameters = {
            "user": {
                "firstName": firstName,
                "lastName": lastName,
                "email": userMailId,
            }
        }
        sheety_user_response_edit = requests.post(url=sheety_users_endpoint, json=sheety_user_parameters)
    else:
        print("Email didn't matched! Try again please.")


def search_engine():
    sheety_user_response = requests.get(url=sheety_users_endpoint)
    user_data = sheety_user_response.json()
    # TODO:     Cheapest flight search
    teq_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
    today_date = datetime.strftime(datetime.now(), "%d/%m/%Y")
    print(today_date)

    for i in range(0, len(sheety_data["prices"])):
        iataCodes = sheety_data["prices"][i]["iataCode"]
        city_names = sheety_data["prices"][i]["city"]
        price = sheety_data["prices"][i]["lowestPrice"]

        for j in range(0, till_days):
            # j = j * 2
            target_date = datetime.strftime(datetime.now() + relativedelta(days=+j), "%d/%m/%Y")
            teq_parameters = {
                "fly_from": "LHR",
                "fly_to": iataCodes,
                "date_from": today_date,
                "date_to": target_date,
                "curr": "EUR"
            }

            teq_response = requests.get(url=teq_search_endpoint, params=teq_parameters,
                                        headers=tequila_apiKey_header)
            teq_data = teq_response.json()
            pp = pprint.PrettyPrinter(indent=4)

            if teq_data['data'][j]['price'] <= price:
                pp.pprint(f"Destination {city_names}, Date: {target_date}, fare: {teq_data['data'][j]['price']}")
                flight_found = True
                # TODO: Sending emails to the users
                if flight_found:
                    for k in range(0, len(user_data["users"])):
                        test_email = user_data["users"][k]["email"]
                        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
                            connection.starttls()
                            connection.login(user=my_email, password=my_pass)
                            connection.sendmail(from_addr=my_email,
                                                to_addrs=test_email,
                                                msg=f"Subject:Cheapest flight rate alert!\n\n Destination {city_names},"
                                                    f" Date: {target_date}, fare: {teq_data['data'][j]['price']}")

            else:
                print(f"In {city_names}, Expected price {price} EUR, No budget flight on {target_date}. "
                      f"Actual fare is: {teq_data['data'][j]['price']} EUR")


ans = input("Welcome to Nas's Flight Club. Have your registered yet? y/n\n")
if ans == "y":
    search_engine()
else:
    user_details()
    search_engine()


