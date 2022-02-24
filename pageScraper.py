import requests
from bs4 import BeautifulSoup

from models.page import Page


class PageScraper:

    _headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    _base_ldlc_url = "https://www.ldlc.com"

    def __init__(self, url):
        self._url = url

    def scrap(self):
        req = requests.get(self._url, self._headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        items = soup.findAll('li', {'class': 'pdt-item'})

        nextPageUrlBtn = soup.find('li', {'class': 'next'})
        if nextPageUrlBtn != None:
            nextPageUrl = self._base_ldlc_url + \
                nextPageUrlBtn.find('a').attrs['href']
        else:
            nextPageUrl = ""

        productsURLs = []
        for item in items:
            productsURLs.append(
                self._base_ldlc_url + item.find('div', {'class': 'pic'}).find('a').attrs['href'])

        return Page(productsURLs, nextPageUrl)
