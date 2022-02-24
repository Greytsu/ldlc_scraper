import unittest
import requests
from models.product import Product
from pageScraper import PageScraper
from postDB import PostDB
from productScraper import ProductScraper
from bs4 import BeautifulSoup


class PageScraperTest(unittest.TestCase):

    _url = "https://www.ldlc.com/fr-be/informatique/pieces-informatique/carte-graphique-interne/c4684/+fv121-19183,19184,19365,19509,19800,19801.html?sort=4"
    _headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    def setUp(self):
        self._products = [
            Product("https://www.ldlc.com/fr-be/fiche/PB00454442.html",
                    "KFA2 GeForce RTX 3080 SG (1-Click OC) LHR",
                    1199.94,
                    "La carte graphique gaming KFA2 GeForce RTX 3080 SG (1-Click OC) LHR bénéficie d'un overclocking d'usine ainsi que de la fonctionnalité 1-Click OC. Elle dispose en outre d'un système de refroidissement ultra-performant à 3 + 1 ventilateurs.",
                    "Rupture"),
            Product("https://www.ldlc.com/fr-be/fiche/PB00438961.html",
                    "Gigabyte GeForce RTX 3070 Ti GAMING OC 8G",
                    1069.95,
                    "La carte graphique Gigabyte GeForce RTX 3070 Ti GAMING OC 8G embarque 8 Go de mémoire vidéo de nouvelle génération GDDR6X. Ce modèle overclocké d'usine bénéficie de fréquences de fonctionnement élevées et d'un système de refroidissement amélioré gage de fiabilité et de performances à long terme.",
                    "En stock")
        ]

    def test_websiteStillUp(self):
        req = requests.get(self._url, self._headers)
        self.assertNotEquals(req, None)

    def test_pageScrap(self):
        pageScraper = PageScraper(self._url)
        page = pageScraper.scrap()

        self.assertTrue(len(page._productURLs) > 0)

    def test_sendPorductsAPI(self):
        postDB = PostDB(self._products)
        response = postDB.post()
        self.assertEqual(response.status_code, 201)
