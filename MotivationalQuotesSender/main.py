import random
import smtplib
import datetime

MY_EMAIL = "laserbeetle1@gmail.com"
PASSWORD = "36214880"

now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as data:
        raw_data = data.readlines()
        quote = random.choice(raw_data)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="laserbeetle1@yahoo.com", msg=f"Subject:Hello\n\n{quote}")

