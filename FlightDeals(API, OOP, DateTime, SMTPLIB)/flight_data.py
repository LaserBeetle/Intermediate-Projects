from notification_manager import NotificationManager


class FlightData:

    def __init__(self):
        pass

    def email_data(self, cities, search_result, index):
        title = cities[index]
        body = search_result['data'][0]['deep_link']
        NotificationManager().send_email(title, body)