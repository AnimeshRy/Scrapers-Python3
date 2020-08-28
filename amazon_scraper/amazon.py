import requests
from bs4 import BeautifulSoup
import re
from page import get_info
import json
# URL = 'https://www.amazon.in/s?k=router+dual+band'


def prices(URL):
    print('Uploading prices...')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    res = requests.get(
        URL, headers=headers)
    search_page = BeautifulSoup(res.text, 'html.parser')
    names = search_page.findAll(
        'a', {'class': 'a-size-base a-link-normal s-no-hover a-text-normal'})
    links = []
    for i in names:
        links.append(f"https://amazon.in/{i.get('href')}")
    for link in links:
        price_dict = get_info(link)
        with open('input.json', 'r+') as file:
            data = json.load(file)
            if price_dict == None:
                pass
            data.update(price_dict)
            file.seek(0)
            json.dump(data, file)
        print('looking for prices..')


if __name__ == "__main__":
    search_param = input('What do you wanna search for ? ')
    amazon_url = f"https://www.amazon.in/s?k={search_param}"
    dicto = {"name": "price"}
    with open('input.json', 'w') as file:
        json.dump(dicto, file)
    prices(amazon_url)
    print('Report Complete.')
