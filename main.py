from pageScraper import PageScraper
from postDB import PostDB
from productScraper import ProductScraper

url = "https://www.ldlc.com/fr-be/informatique/pieces-informatique/carte-graphique-interne/c4684/+fv121-19183,19184,19365,19509,19800,19801.html?sort=4"


while True:
    pageScraper = PageScraper(url)
    page = pageScraper.scrap()

    productScraper = ProductScraper(page._productURLs)
    products = productScraper.scrap()

    postDB = PostDB(products)
    postDB.post()

    url = page._nextPageURL

    if page._nextPageURL == "":
        break
