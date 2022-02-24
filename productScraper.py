import requests
from bs4 import BeautifulSoup
import re

from models.product import Product


class ProductScraper:

    _headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    def __init__(self, productsURLs):
        self._productsURLs = productsURLs

    def scrap(self):
        products = []

        # for productURL in self._productsURLs:
        for i in range(4):

            productReq = requests.get(self._productsURLs[i], self._headers)
            productSoup = BeautifulSoup(productReq.content, 'html.parser')
            productBloc = productSoup.find(
                'div', {'class': 'sbloc product-bloc'})

            title = productBloc.find('h1', {'class': 'title-1'}).text.strip()
            desc = productBloc.find('p', {'class': 'desc'}).text.strip()
            price = re.findall('\d|[.]', productBloc.find('div', {'class': 'price'}).find(
                'div', {'class': 'price'}).text.replace("€", "."))
            priceFloat = float(''.join(price))
            stock = productBloc.find('div', {'class': 'modal-stock-web'}).text

            products.append(
                Product(self._productsURLs[i], title, priceFloat, desc, stock))

        return products
