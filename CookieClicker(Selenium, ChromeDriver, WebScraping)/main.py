from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/User/PycharmProjects/chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
numbers = driver.find_element(by=By.ID, value="toggleNumbers")
numbers.click()
flash = driver.find_element(by=By.ID, value="toggleFlash")
flash.click()


def click_cookie():
    cookie = driver.find_element(by=By.ID, value="cookie")
    cookie.click()


def upgrade():
    suffix = ["Time machine", "Portal", "Alchemy lab", "Shipment", "Mine", "Factory", "Grandma", "Cursor"]
    current_cookies = driver.find_element(by=By.ID, value="money").text
    for item in suffix:
        upgrades = driver.find_element(by=By.ID, value=f"buy{item}")
        if int(upgrades.text.split("\n")[0].split("-")[1].replace(",","")) <= int(current_cookies.replace(",","")):
            upgrades.click()
    game_start()


def game_start():
    upgrade_timeout = time.time() + 5
    while True:
        click_cookie()
        if time.time() >= upgrade_timeout:
            upgrade()


game_start()
