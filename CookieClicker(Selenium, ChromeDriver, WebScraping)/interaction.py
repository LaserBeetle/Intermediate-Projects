from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/User/PycharmProjects/chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

#clicking a link with CSS Selector
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# articles = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# articles.click()

#clicking a link directly with Link Text
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# contents = driver.find_element(by=By.LINK_TEXT, value="Contents")
# contents.click()

#typing on the search bar and searching an element automatically
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# search_bar = driver.find_element(by=By.NAME, value="search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

#automatically filling 3 forms and clicking a button
# driver.get("http://secure-retreat-92358.herokuapp.com/")
# forms = driver.find_elements(by=By.CLASS_NAME, value="form-control")
#
# for index in range(len(forms)):
#     forms[index].send_keys("Guilherme")
#     if index == 2:
#         forms[index].send_keys("@Guilherme")
#
# button = driver.find_element(by=By.CLASS_NAME, value="btn")
# button.click()

driver.quit()
