import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data = DataManager().get_data()

for item in data["prices"]:
    if item["iataCode"] == "":
        city_id = item["id"]
        city_code = FlightSearch().get_code(item)["locations"][0]["code"]
        DataManager().edit_code(city_code, city_id)

today = datetime.date.today()
future_day = today.day
future_month = (today.month + 6) % 12
future_year = today.year + ((today.month + 6) // 12)

six_months_later = datetime.date(future_year, future_month, future_day)

teq_params = {
    "fly_from": "LON",
    "fly_to": "",
    "date_from": f"{today.strftime('%d/%m/%Y')}",
    "date_to": f"{six_months_later.strftime('%d/%m/%Y')}",
    "max_stopovers": 0,
    "flight_type": "round",
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28
}

for index in range(len(data["prices"])):
    teq_params["fly_to"] = data["prices"][index]["iataCode"]
    search_result = FlightSearch().search_prices(teq_params)

    try:
        low_price = search_result["data"][0]["price"]
    except IndexError:
        teq_params["max_stopovers"] = 3
        search_result = FlightSearch().search_prices(teq_params)
        try:
            low_price = search_result["data"][0]["price"]
        except IndexError:
            continue

    try:
        price_on_record = data["prices"][index]["lowestPrice"]
    except KeyError:
        city_index = index + 2
        DataManager().edit_price(low_price, city_index)
        data["prices"][index]["lowestPrice"] = low_price

    if data["prices"][index]["iataCode"] == "TYO":
        low_price = 1
    elif low_price < data["prices"][index]["lowestPrice"]:
        users_data = DataManager().get_users()
        FlightData().email_data(data["prices"], search_result, index, users_data)
