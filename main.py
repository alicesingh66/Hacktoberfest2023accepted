import requests
from twilio.rest import Client

from datetime import *


account_sid = "ACdff2d5034ebb911ec607e30a7bff18cf"
auth_token = "45330946240787ed040a9a63d871a851"

now_h = datetime.now()
now_hour = now_h.hour
print(now_hour)
API_KEY = '1f686eed9bdbdd0749bc9480ac123790'
LINK = 'https://api.openweathermap.org/data/2.5/weather'

weather_meters = {
    'lat': 44.34,
    'lon': 10.99,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

while now_hour == 7:
    response = requests.get(LINK, params=weather_meters)
    response.raise_for_status()
    data = response.json()
    now_code = int(data["weather"][0]["id"])
    if now_code >= 500 or now_code <= 700:
        print('Take an umbrella')
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='It is a Rainy Day. Take an ☂️',
            from_='Generated Twillio',
            to='Your Number'
        )



# while now_hour == 7:
