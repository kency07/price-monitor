import csv
import os 
from datetime import datetime

PRODUCTS_HEADERS = [
    "product_id",
    "product_name",
    "site",
    "product_url",
    "target_price"
]
HISTORY_HEADERS = [
    "timestamp",
    "product_id",
    "product_name",
    "site",
    "price",
    "price_drop"
]

def read_products(file_path):
    '''read products.csv and return list of  dicts''' 
    product = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"products file not found: {file_path}")

    with open (file_path, newline= "", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames != PRODUCTS_HEADERS:
            raise ValueError("products.csv headers do not match expected formate")
        
        for row in reader:
            if not row.get("product_id") or not row.get("product_url") or not row.get("site"):
                continue # skip invalid row safely

            product.append(row)

    return product
def ensure_history_file(file_path):
    """Create price_history.csv if it does not exist"""
    if not os.path.exists(file_path):

        with open(file_path, "w", newline= "", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HISTORY_HEADERS)

def get_last_price(file_path, product_id):
     """Return last recorded price for a product_id, or None"""
     if not os.path.exists(file_path):
         return None
     
     last_price = None

     with open(file_path, newline= "", encoding="utf-8") as f:
         reader = csv.DictReader(f)

         for row in reader:
            if row.get("product_id") == str(product_id):
                last_price = row.get("price")

            return float(last_price) if last_price else None

def append_price_history(
    file_path,
    product_id,
    product_name,
    site,
    price,
    price_drop
):
    """Append a new price record"""
    ensure_history_file(file_path)

    with open(file_path, "a", newline= "", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
    product_id,
    product_name,
    site,
    price,
    price_drop])






                

