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

    page_numbers_1 = soup.find('a', href="index1_page_1.html")
    page_numbers_2 = soup.find('a', href="index1_page_2.html")
    page_numbers_3 = soup.find('a', href="index1_page_3.html")
    page_numbers_4 = soup.find('a', href="index1_page_4.html")

    watchs = soup.find('a', href="index1_page_1.html")
    phones = soup.find('a', href="index2_page_1.html")
    mice = soup.find('a', href="index3_page_1.html")
    hdd = soup.find('a', href="index4_page_1.html")
    headphones = soup.find('a', href="index5_page_1.html")

    url = 'https://parsinger.ru/html/'

    with open('index.txt', mode='w', encoding='utf-8') as file:
        for name, price in zip(names, prices):
            file.write(f'{name} - {price}\n')

        if page_numbers_1:
            page_numbers_1_text =(page_numbers_1['href'])
            file.write(f'\nСсылка на первую страницу - {page_numbers_1_text}\n')
        if page_numbers_2:
            page_numbers_2_text =(page_numbers_2['href'])
            file.write(f'Ссылка на первую страницу - {page_numbers_2_text}\n')
        if page_numbers_3:
            page_numbers_3_text =(page_numbers_3['href'])
            file.write(f'Ссылка на первую страницу - {page_numbers_3_text}\n')
        if page_numbers_4:
            page_numbers_4_text =(page_numbers_4['href'])
            file.write(f'Ссылка на первую страницу - {page_numbers_4_text}\n')

        if watchs:
            page_watchs_text =(watchs['href'])
            watch = 'https://parsinger.ru/html/' + page_watchs_text
            file.write(f'\nСсылка на часы - {watch}\n')
        if phones:
            page_phones_text =(phones['href'])
            phone = 'https://parsinger.ru/html/' + page_phones_text
            file.write(f'Ссылка на телефоны - {phone}\n')
        if mice:
            page_mice_text =(mice['href'])
            mic = 'https://parsinger.ru/html/' + page_mice_text
            file.write(f'Ссылка на мыши - {mic}\n')
        if hdd:
            page_hdd_text =(hdd['href'])
            hddd = 'https://parsinger.ru/html/' + page_hdd_text
            file.write(f'Ссылка на HDD - {hddd}\n')
        if headphones:
            page_headphones_text =(headphones['href'])
            headphone = 'https://parsinger.ru/html/' + page_headphones_text
            file.write(f'Ссылка на наушники - {headphone}\n')





    pass




URL = 'https://parsinger.ru/html/index1_page_1.html'
html = get_html(URL)
pars_html(html)
