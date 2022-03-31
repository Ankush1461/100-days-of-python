# Rain SMS Alert Program

import os
import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "OWM_API_KEY"
account_sid = "YOUR ACCOUNT SID"
auth_token = "AUTH_TOKEN"

weather_params = {
    "lat": "LATITUDE",
    "lon": "LONGITUDE",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain. Get an umbrella.",
        from_='YOUR TWILIO VIRTUAL NUMBER',
        to='YOUR TWILIO VERIFIED REAL NUMBER'
    )
    print(message.status)
