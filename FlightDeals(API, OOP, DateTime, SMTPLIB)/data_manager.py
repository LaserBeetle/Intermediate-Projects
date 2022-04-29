import requests


class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co"
        self.SHEETY_KEY = "b28aa3166502359ee89ac4034dcb5431"
        self.SHEETY_LOCATION = "flightDeals/prices"

    def get_data(self):
        sheety_response = requests.get(url=f"{self.SHEETY_ENDPOINT}/{self.SHEETY_KEY}/{self.SHEETY_LOCATION}")
        return sheety_response.json()

    def edit_code(self, city_code, city_id):
        put_config = {
            "price": {
                "iataCode": f"{city_code}"
            }
        }
        requests.put(url=f"{self.SHEETY_ENDPOINT}/{self.SHEETY_KEY}/{self.SHEETY_LOCATION}/{city_id}", json=put_config)

    def edit_price(self, low_price, city_index):
        put_config = {
            "price": {
                "lowestPrice": low_price
            }
        }
        requests.put(url=f"{self.SHEETY_ENDPOINT}/{self.SHEETY_KEY}/{self.SHEETY_LOCATION}/{city_index}", json=put_config)