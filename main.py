# This file scrapes the Y Combinator and returns the highest voted article with corresponding link,
# and the number of up votes.
import requests
from bs4 import BeautifulSoup
# https://news.ycombinator.com/news
# appbrewery.github.io/news.ycombinator.com

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
subline_tag = soup.find_all(name="span", class_="score")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.select("a")[0].get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_upvote =  max(article_upvotes)
highest_upvote_index = article_upvotes.index(highest_upvote)

print(article_texts[highest_upvote_index])
print(article_links[highest_upvote_index])
print(article_upvotes[highest_upvote_index])
