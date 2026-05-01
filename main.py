import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

params = {
    "lat" : 30.6,
    "lon": 94.25,
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
        from_="whatsapp:+14155238886",
        to="whatsapp:+16572466100",
    )
