import smtplib

USER = "laserbeetle1@gmail.com"
PASS = "36214880"
EMAIL = "laserbeetle1@gmail.com"


def error_margin(iss_lat, iss_long, my_lat, my_long):
    if my_lat-5 <= iss_lat <= my_lat+5 and my_long-5 <= iss_long <= my_long+5:
        return True
    else:
        return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject:Look up!\n\nThe ISS is overhead.")