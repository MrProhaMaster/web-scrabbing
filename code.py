import requests
import bs4
from fake_headers import Headers
headers = Headers(os="win", headers=True).generate()
url = 'https://habr.com/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
response = requests.get(url, headers=headers)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")
for article in articles:
    tags = article.find_all(class_="tm-article-snippet__hubs-item-link")
    tags = [tag.find("span").text.lower() for tag in tags]
    topic = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").find("span").text
    time = article.find(class_="tm-article-snippet__datetime-published").find("time").text
    link = article.find(class_="tm-article-snippet__readmore").attrs["href"]
    for key in KEYWORDS:
        if key in tags:
            print(f"{time} - {topic} - {link}")