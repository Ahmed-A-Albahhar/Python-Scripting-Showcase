import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Securely fetching credentials from environment variables
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
API_KEY = os.environ.get("OWM_API_KEY")

# Masking personal location data via environment variables
MY_LAT = float(os.environ.get("MY_LAT", 26.58))
MY_LONG = float(os.environ.get("MY_LONG", 50.05))
TARGET_PHONE = os.environ.get("MY_PHONE_NUMBER", "+1234567890")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

# Parsing JSON payload for weather condition codes
for n in range(len(weather_data['list']) - 1):
    condition_code = int(weather_data['list'][n]['weather'][0]['id'])
    if condition_code < 700:
        will_rain = True

# Trigger SMS notification via Twilio API if rain is forecasted
if will_rain:
    proxy_client = TwilioHttpClient()

    # Optional proxy setup for specific deployment environments
    if 'https_proxy' in os.environ:
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body='Ahoy 👋, It is going to rain today so remember to bring an umbrella.',
        from_='whatsapp:[YOUR_TWILIO_NUMBER]',
        to=f'whatsapp:{TARGET_PHONE}'
    )
    print(f"Message Status: {message.status}")
