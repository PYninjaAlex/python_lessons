import requests
from bs4 import BeautifulSoup as bs

book_num = 0
for i in range(1,51):
    source = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html').text
    soup = bs(source, 'html.parser')
    print(f'\t\tСтраница номер: {i}')
    for article in soup.find_all('article', class_='product_pod'):
        book_num += 1
        title = article.h3.a['title']
        price = article.find('p', class_='price_color').text
        rate = article.p['class'][-1]
        print(f'Книга номер {book_num}: {title}\n\t Цена: {price[2:]}; Рейтинг: {rate}')
