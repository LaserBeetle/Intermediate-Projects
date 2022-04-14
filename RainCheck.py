import requests
from twilio.rest import Client

API_KEY = "a4b380bc861cebcf50741a00fcdfcf35"
MY_LAT = "-23.071204"
MY_LON = "-45.560736"
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

ACCOUNT_SID = "AC853414071d6901457119f4617787bc16"
AUTH_TOKEN = "c09bd1369d0a8a764a172519d6fd2105"

parameters = {"lat": MY_LAT, "lon": MY_LON, "appid": API_KEY, "exclude": "current,minutely,daily"}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

next_twelve = data["hourly"][0:12]
weather_id = [item["weather"][0]["id"] for item in next_twelve if item["weather"][0]["id"] < 700]

if len(weather_id) > 0:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Bring an Umbrella.",
        from_="+16892158528",
        to="+5512991030394"
    )
    print(message.status)
