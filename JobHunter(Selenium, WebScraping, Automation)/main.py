from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_driver_path = "C:/Users/User/PycharmProjects/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/"
           "?f_AL=true&geoId=106057199&keywords=python%20junior&location=Brazil")

#logging in LinkedIn
login = driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary")
login.click()
username = driver.find_element(by=By.ID, value="username")
username.send_keys("guilherme.dsr18@gmail.com")
password = driver.find_element(by=By.ID, value="password")
password.send_keys("gsr180594")
login2 = driver.find_element(by=By.CLASS_NAME, value="btn__primary--large")
login2.click()

#indexing the job listings following the pre-requisites in the url
jobs = driver.find_elements(by=By.CLASS_NAME, value="jobs-search-results__list-item")

#clicking each listing to open the specific job info
for item in jobs:
    item.click()
    #waiting and scrolling page to load every item
    time.sleep(2)
    ActionChains(driver).move_to_element(item).scroll_by_amount(0, 200).perform()
    save = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button span")

    #saving the job listing if it isnt saved yet
    if save.text == "Save":
        save.click()
        print("Job saved")

driver.quit()
