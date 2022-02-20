import requests
from bs4 import BeautifulSoup
import re

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

url = "https://www.ldlc.com/fr-be/informatique/pieces-informatique/carte-graphique-interne/c4684/+fv121-19183,19184,19365,19509,19800,19801.html?sort=4"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

items = soup.findAll('li', {'class': 'pdt-item'})

productsURLs = []
for item in items:
    productsURLs.append("https://www.ldlc.com" + item.find('div', {'class': 'pic'}).find('a').attrs['href'])

for productURL in productsURLs:

    productURL = "https://www.ldlc.com/fr-be/fiche/PB00454442.html"
    productReq = requests.get(productURL, headers)
    productSoup = BeautifulSoup(productReq.content, 'html.parser')
    productBloc = productSoup.find('div', {'class': 'sbloc product-bloc'})

    title = productBloc.find('h1', {'class': 'title-1'}).text.strip()
    desc = productBloc.find('p', {'class': 'desc'}).text.strip()
    price = re.findall('\d|[.]', productBloc.find('div', {'class': 'price'}).find('div', {'class': 'price'}).text.replace("€", "."))
    priceFloat = float(''.join(price))
    stock = productBloc.find('div', {'class': 'modal-stock-web'}).text

#Mock
# title = "KFA2 GeForce RTX 3080 SG (1-Click OC) LHR"
# desc = "La carte graphique gaming KFA2 GeForce RTX 3080"
# price = "1 199.94"
# stock = "Sous 7 jours"

print("")
print(title)
print(desc)
print(priceFloat)
print(stock)
