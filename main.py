import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
phone_from = os.environ.get("PHONE_FROM")
phone_to = os.environ.get("PHONE_TO")

params = {
    "lat" : 33.8,
    "lon": -118.009,
    "cnt": 4,
    "units": "imperial",
    "appid": api_key
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=params)
response.raise_for_status()
data = response.json()
li = data['list']
rain = False

for i in li:
    # if i['weather'][0]['id'] < 700:
    condition_code = i['weather'][0]['id']
    if condition_code < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hewo, it will rain on in the next 12 hours",
        from_=phone_from,
        to=phone_to,
    )
