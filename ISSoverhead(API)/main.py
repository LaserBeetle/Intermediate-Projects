import requests
from datetime import datetime
import time
import config

MY_LAT = -23.030590
MY_LONG = -45.548611

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data_iss = response.json()

iss_latitude = float(data_iss["iss_position"]["latitude"])
iss_longitude = float(data_iss["iss_position"]["longitude"])

overhead = config.error_margin(iss_latitude, iss_longitude, MY_LAT, MY_LONG)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data_sun = response.json()
sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
now_hour = time_now.hour

if now_hour > sunset or now_hour < sunrise:
    while overhead:
        config.send_email()
        time.sleep(600)
