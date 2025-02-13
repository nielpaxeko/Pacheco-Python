from operator import indexOf
from bs4 import BeautifulSoup
import requests

# Get soup from online html file
response = requests.get("https://news.ycombinator.com/news")
webpage = response.text 
soup = BeautifulSoup(webpage, "html.parser")

# Get title of first article
all_articles = soup.find_all("span", class_="titleline")
 
article_texts = []
article_links = []
 
# Get articles names, links and upvotes
for article in all_articles:
    text = article.getText()
    article_texts.append(text)
    link = article.find("a")["href"]
    article_links.append(link)
    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# Get most upvoted article's title and link 
index = indexOf(article_upvotes, max(article_upvotes)) # Get index of most upvoted articles in article_upvotes
print(f"Article name: {article_texts[index]}") 
print(f"Link to article: {article_links[index]}") 
print(f"Total upvotes: {article_upvotes[index]}") 