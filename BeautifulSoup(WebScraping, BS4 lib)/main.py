from bs4 import BeautifulSoup
import requests

#
# with open ("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.a)
# print(soup)
# print(soup.prettify)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# heading = soup.select(".heading")
# print(heading)

response = requests.get("https://news.ycombinator.com/news")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for anchor_tag in articles:
    text = anchor_tag.getText()
    article_texts.append(text)
    link = anchor_tag.get("href")
    article_links.append(link)

articles_upvote = [int(upvotes.getText().split()[0]) for upvotes in soup.find_all(name="span", class_="score")]

index = -1
highest_upvote = 0
highest_index = 0
for number in articles_upvote:
    index += 1
    if number > highest_upvote:
        highest_upvote = number
        highest_index = index

print(article_texts[highest_index])
print(article_links[highest_index])
print(articles_upvote[highest_index])