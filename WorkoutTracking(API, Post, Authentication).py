import requests
import datetime
from requests.auth import HTTPBasicAuth

NUTRI_ID = "364539d1"
NUTRI_KEY = "8671c51b6d6849299339975d32c2fb1f"
SHEETY_USER = "laserbeetle"
SHEETY_PASS = "ABCabc123456"

NUTRI_HEADERS = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_KEY,
}

SHEETY_HEADERS = {
    "Authorization": "Basic bGFzZXJiZWV0bGU6QUJDYWJjMTIzNDU2"
}


response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         data={"query": input("What exercise did you want to log?\n")},
                         headers=NUTRI_HEADERS)
result = response.json()

for activity in result["exercises"]:
    sheety_body = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%X"),
            "exercise": activity["name"],
            "duration": activity["duration_min"],
            "calories": activity["nf_calories"]
        }
    }
    sheety = requests.post(url="https://api.sheety.co/b28aa3166502359ee89ac4034dcb5431/workoutTracking/workouts",
                           json=sheety_body, headers=SHEETY_HEADERS,
                           auth=HTTPBasicAuth(SHEETY_USER, SHEETY_PASS))
    print(sheety.text)
