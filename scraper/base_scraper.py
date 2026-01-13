import requests
from bs4 import BeautifulSoup
import re
import time
import random


class BaseScraper:
    USER_AGENTS = [
        "MozilLa/5.0(Windows NT 10.0; Win64; x64)",
        "MozilLa/5.0 (X11; Linux x86_64)",
        "MozilLa/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    ]

    def __init__(self, timeout=10):  # Python constructors must have double underscores
        self.timeout = timeout

    def fetch_page(self, url):
        headers = {
            "User-Agent": random.choice(self.USER_AGENTS),
            "Accept-Language": "en-US, en:q=0.9",
        }
        try:
            response = requests.get(url, headers=headers, timeout=self.timeout)

            response.raise_for_status()
            time.sleep(random.uniform(1, 3))  # polite delay

            return response.text
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def clean_price(self, raw_price):
        """
        Extract numeric value from price.
        Examples:
        '₹54,999' -> 54999.0

        """

        # Case 1: invalid or empty
        if not isinstance(raw_price, str) or not raw_price.strip():
            return None

        # Case 2: raw_price is not a string or empty
        # if not isinstance(raw_price, str) or not raw_price.strip():
            # return None
            
        # Case 2: string price
        clean_price= raw_price.replace(",", "")
        match = re.search(r"\d+(?:\.\d+)?", clean_price)
        return float(match.group()) if match else None

    def extract_price(self, html, selector, attribute=None):

        if not selector:
            return None

        try:
            soup = BeautifulSoup(html, "html.parser")
            element = soup.select_one(selector)
        except Exception:
            return None

        if not element:
            return None

        if attribute:
            return element.get(attribute)

        return element.get_text(strip=True)

    def get_price(self, url, selector, attribute=None):

        html = self.fetch_page(url)
        if not html:
            return None

        raw_price = self.extract_price(html, selector, attribute)
        return self.clean_price(raw_price)
