from utils.csv_handler import read_products, get_last_price, append_price_history
from scraper.site_a import SiteAScraper
from scraper.site_b import SiteBScraper
from config.sites import SITE_CONFIG
from datetime import datetime


SCRAPER_MAP = {"site_a": SiteAScraper, "site_b": SiteBScraper}


def main():
    products = read_products("data/products.csv")

    for product in products:
        product_id = product["product_id"]
        site_key = product["site"]
        url = product["product_url"]

        scraper_class = SCRAPER_MAP.get(site_key)
        if not scraper_class:
            print(f"[skip] unsupported site: {site_key}")
            continue

        scraper = scraper_class(SITE_CONFIG[site_key])
        current_price = scraper.get_product_price(url)

        if current_price is None:
            print(f"[Error] Failed to fetch price for product: {product_id}")
            continue

        last_price = get_last_price("data/price_history.csv", product_id)

        append_price_history(
            "data/price_history.csv",
            product_id,
            current_price,
            datetime.now().isoformat(),
        )
        if last_price and current_price < last_price:
            print(
                f"[drop] product {product_id} price: "
                f"{last_price} -> {current_price}"
            )
        else:
            print(f"[ok] product {product_id}: {current_price}")


if __name__ == "__main__":
    main()
