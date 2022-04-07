import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "laserbeetle1@gmail.com"
MY_PASSWORD = "36214880"

birthdays = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
now_month = now.month
now_day = now.day

for row in pandas.DataFrame.iterrows(birthdays):
    if row[1]["month"] == now_month and row[1]["day"] == now_day:
        num = random.randint(1, 3)

        with open(f"letter_templates/letter_{num}.txt", "r") as data:
            template = data.read()
            message = template.replace("[NAME]", f"{row[1]['name']}")

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=row[1]["email"], msg=f"Subject:Happy Birthday!\n\n{message}")
