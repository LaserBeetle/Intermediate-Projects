import requests
import smtplib
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_KEY = "GT2NMBDDLK3NM3MM"
NEWS_KEY = "c4bc31d34bde4b51a9c76fa6ab386dd9"
MY_USER = "laserbeetle1@gmail.com"
MY_PASS = "AaBbCc12345"

today = datetime.datetime.today()
yesterday = today-datetime.timedelta(days=1)
daybefore = today-datetime.timedelta(days=2)
yesterday_date = str(yesterday).split(" ")[0]
daybefore_date = str(daybefore).split(" ")[0]

AV_PARAMS = {"function": "TIME_SERIES_DAILY",
             "symbol": STOCK,
             "apikey": ALPHAVANTAGE_KEY}

NEWS_PARAMS = {"qInTitle": COMPANY_NAME,
               "apiKey": NEWS_KEY}

av_response = requests.get("https://www.alphavantage.co/query?", params=AV_PARAMS)
av_response.raise_for_status()
av_data = av_response.json()

yesterday_close = av_data["Time Series (Daily)"][yesterday_date]["4. close"]
daybefore_close = av_data["Time Series (Daily)"][daybefore_date]["4. close"]
difference = (float(daybefore_close) - float(yesterday_close)) / float(daybefore_close) * 100

if difference >= 5 or difference <= -5:
    news_response = requests.get("https://newsapi.org/v2/everything?", params=NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()

    if difference > 0:
        message = f"{STOCK}: +{difference}%\n\n"
    else:
        message = f"{STOCK}: -{difference}%\n\n"

    for article in news_data["articles"][:3]:
        message += f"{article['description']}: {article['url']}\n"

    # TODO. 1: FIND A WAY TO FORMAT THIS TEXT!!
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #     connection.starttls()
    #     connection.login(user=MY_USER, password=MY_PASS)
    #     connection.sendmail(from_addr=MY_USER, to_addrs=MY_USER, msg=f"Subject:TESLA Stock Alert!\n\n{message}")
