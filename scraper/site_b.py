from scraper.base_scraper import BaseScraper

class SiteBScraper(BaseScraper):
    SITE_KEY = "b_site"


    def __init__(self,site_config):
        super().__init__() 
        self.config = site_config

    def get_product_price(self,url):
        selector = self.config["price_selector"]
        attribute = self.config.get("price_attribute")
        return self.get_price(url, selector,attribute)