import requests
import re
from bs4 import BeautifulSoup
import json

# URL = 'https://www.amazon.in/TP-Link-Archer-C20-Wireless-Router/dp/B0759QMF85/ref=sr_1_7?dchild=1&keywords=router&qid=1592651166&sr=8-7'


def get_info(URL):
    count = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    try:
        res = requests.get(URL, headers=headers)
    except:
        count += 1
        pass
    if count != 1:
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            name = soup.find('span', {'id': 'productTitle'}).text.strip()
            price = soup.find(
                'span', {'id': 'priceblock_ourprice'}).text.strip()
            price_dict = {name: price}
            if price_dict != None:
                return price_dict
        except:
            pass
    return None

# get_info(URL)
