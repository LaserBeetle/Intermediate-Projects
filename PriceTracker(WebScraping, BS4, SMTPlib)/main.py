import requests
import bs4
import smtplib


USER = "laserbeetle1@gmail.com"
PASS = "!4mL33tAF"
URL = "https://www.amazon.com/ASUS-GeForce-i7-11370H-Windows-TUF516PE-AB73/dp/B08XPC3WFQ/ref=psdc_13896617011_t3_B09127DDVT?th=1"
HEADERS = {
    "Content-Type": "application/json",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}


response = requests.get(url=URL, headers=HEADERS)
soup = bs4.BeautifulSoup(response.text, "html.parser")

#Find the price in the soup, separate it from the $ sign and turn into Float datatype
price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])

if price < 750.00:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PASS)
        connection.sendmail(from_addr=USER,
                            to_addrs=USER,
                            msg=f"Subject: New deal for Acer Notebook!\n\nYour tracked item is listed for "
                                f"${price}! It's under your tracked value. Check it out.\n{URL}")
