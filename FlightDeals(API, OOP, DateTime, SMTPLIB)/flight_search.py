import requests


class FlightSearch:

    def __init__(self):
        self.TEQUILA_KEY = "f2V_3yg_VLd-j-adk6KIRSorqMjPTbUv"
        self.TEQUILA_ENDPOINT = "http://tequila-api.kiwi.com"
        self.teq_headers = {"apikey": self.TEQUILA_KEY}
        self.teq_body = {}

    def get_code(self, item):
        city_name = item["city"]
        self.teq_body["term"] = city_name
        teq_response = requests.get(url=f"{self.TEQUILA_ENDPOINT}/locations/query", headers=self.teq_headers, params=self.teq_body)
        return teq_response.json()

    def search_prices(self, teq_params):
        teq_response = requests.get(url=f"{self.TEQUILA_ENDPOINT}/v2/search?", headers=self.teq_headers, params=teq_params)
        return teq_response.json()
