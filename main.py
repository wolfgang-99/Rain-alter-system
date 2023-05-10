import requests
import os

os.environ["api_key"] = "a5a8bb8225430ab9f13ce1a2c160c892"
api = "https://api.openweathermap.org/data/3.0/onecall"
param = {
    "lat": 6.444550,
    "lon": 7.49018,
    "appid": os.environ["api_key"],
    "exclude": "current,minutely,daily"
}
response = requests.get(api, params=param)
response.raise_for_status()
data = response.json()

will_rain = False
weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an unblrella")

print(data)
