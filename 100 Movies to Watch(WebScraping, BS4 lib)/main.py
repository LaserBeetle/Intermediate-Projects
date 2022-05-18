import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
web_data = response.text

soup = BeautifulSoup(web_data, "html.parser")
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

with open("movies.txt", "w") as file:
    for title in titles[::-1]:
        file.write(f"{title}\n")
