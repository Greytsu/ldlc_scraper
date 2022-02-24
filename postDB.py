import json
import requests
from models.product import Product


class PostDB:
    _products = []
    _headers = {'Content-Type': 'application/json',
                'Accept': 'application/json'}
    _url = "http://localhost:8080/product_crud/api/v1/products"

    def __init__(self, products):
        self._products = products

    def post(self):
        print([product.__dict__ for product in self._products])
        return requests.post(self._url, data=json.dumps(
            [product.__dict__ for product in self._products]), headers=self._headers)
