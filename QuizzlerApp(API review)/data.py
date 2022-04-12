import requests

parameters = {"amount": 10, "type": "boolean", "category": 31}

data = requests.get(url="https://opentdb.com/api.php?", params=parameters)
data.raise_for_status()
response = data.json()

question_data = response["results"]