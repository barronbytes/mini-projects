import requests
from bs4 import BeautifulSoup as bs


class Pagination():


    @staticmethod
    def calc_page_count(soup: bs) -> int:
        parent_tag = soup.select_one("ul.pagination")
        anchors = parent_tag.select("a.page-link")
        return int(anchors[-2].text)


    @staticmethod
    def scrape_products(url: str) -> list[str]:
        soup = Pagination.create_soup(url)
        products = soup.select("a.title")
        return [p.get("title") for p in products]


    @staticmethod
    def scrape_prices(url: str) -> list[str]:
        soup = Pagination.create_soup(url)
        parent_tags = soup.select("div.caption")
        price_tags = [pt.select_one("span[itemprop='price']") for pt in parent_tags] # cannot use span.price !!!
        return [pt.text.strip() for pt in price_tags]


    @staticmethod
    def create_soup(url: str) -> bs:
        r = requests.get(url)
        return bs(r.content, "lxml")     


    @staticmethod
    def generate_report(products: dict[int, list[str]], prices: dict[int, list[str]]) -> None:
        for key in products:
            for product, price in zip(products[key], prices[key]):
                print(f"Computer: {product}, Price: {price}")


    @staticmethod
    def brain(url: str) -> None:
        soup = Pagination.create_soup(url)
        page_count = Pagination().calc_page_count(soup)
        page_urls = [f"{url}?page={str(n)}" for n in range(1, page_count+1)]
        products = { index:Pagination.scrape_products(url) for index, url in enumerate(page_urls, start=1) }
        prices = { index:Pagination.scrape_prices(url) for index, url in enumerate(page_urls, start=1) }
        Pagination.generate_report(products=products, prices=prices)
