import smtplib


class NotificationManager:
    def __init__(self):
        self.USER = "laserbeetle1@gmail.com"
        self.PASS = "!4mL33tAF"
        self.EMAIL = "laserbeetle1@gmail.com"

    def send_email(self, title, body):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.USER, password=self.PASS)
            connection.sendmail(from_addr=self.EMAIL, to_addrs=self.EMAIL,
                                msg=f"Subject:New deal to {title}!\n\n{body}")
