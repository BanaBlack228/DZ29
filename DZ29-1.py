import requests
import json
from bs4 import BeautifulSoup as BS
from requests.exceptions import ConnectionError

def get_html(url: str) -> str:
    response = requests.get(url)
    status = response.status_code
    print(f'Код ответа: {status}')
    html = response.text
    return html

def pars_html(html: str):
    soup = BS(html, 'html.parser')
    names = []
    prices = []

    watch_name = soup.find_all('a', class_='name_item')
    for name in watch_name:
        watch_name_text = name.text.encode('latin1').decode('utf-8')
        names.append(watch_name_text)

    price_watch = soup.find_all('p', class_='price')
    for price in price_watch:
        price_watch_text = price.text.encode('latin1').decode('utf-8')
        prices.append(price_watch_text)

    with open('index.txt', mode='w', encoding='utf-8') as file:
        for name, price in zip(names, prices):
            file.write(f'{name} - {price}\n')





    pass





URL = 'https://parsinger.ru/html/index1_page_1.html'
html = get_html(URL)
pars_html(html)
