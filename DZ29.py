import requests
from bs4 import BeautifulSoup
import json


def scrape_product_names_and_prices(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', class_='product')
    results = []

    for product in products:
        title = product.find('a', class_='title').text.strip()
        price = product.find('p', class_='price').text.strip()
        results.append({'title': title, 'price': price})

    return results


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=4)


def main():
    url = 'https://parsinger.ru/html/index1_page_1.html'
    products_info = scrape_product_names_and_prices(url)
    save_to_json(products_info, 'products.json')
    print(f"Scraped {len(products_info)} products and saved to products.json.")


if __name__ == "__main__":
    main()
