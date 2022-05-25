from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/User/PycharmProjects/chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

#get price of the item
# driver.get("https://www.amazon.com/ASUS-GeForce-i7-11370H-Windows-TUF516PE-AB73/dp/B08XPC3WFQ/ref=psdc_13896617011_t3_B09127DDVT?th=1")
# price = driver.find_element(by=By.CSS_SELECTOR, value="span.a-price-whole")
# print(price.text)

#get the placeholder on the search bar
# driver.get("https://www.python.org/")
# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

#get the documentation text
# driver.get("https://www.python.org/")
# docs = driver.find_element(by=By.XPATH, value="//*[@id='content']/div/section/div[2]/div[3]/p[2]/a")
# print(docs.text)

#get a dictionary from the upcoming events
# driver.get("https://www.python.org/")
#using XPATH and dict comprehension
# dates = [date.text.split("\n") for date in driver.find_elements(by=By.XPATH, value="//*[@id='content']/div/section/div[3]/div[2]/div/ul/li")]
# events = {index: {"time": dates[index][0], "name": dates[index][1]} for index in range(len(dates))}

#using CSS SELECTOR and for loops
# events_time = [element.text for element in driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")]
# events_name = [element.text for element in driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")]
# events = {}
#
# for index in range(len(events_time)):
#     events[index] = {
#         "time": events_time[index],
#         "name": events_name[index]
#     }
# print(events)

driver.quit()