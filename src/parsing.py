import requests
from bs4 import BeautifulSoup as bs

with open('simple.html') as html_file:
    soup = bs(html_file, 'html.parser')

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    summary = article.p.text
    print(headline)
    print(summary)
    print()