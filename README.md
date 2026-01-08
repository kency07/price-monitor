# Price Monitor (Multi-Site Product Price Tracker)

A scalable **Python-based product price monitoring system** that tracks prices across multiple e-commerce sites using a clean, modular architecture. The project is designed as a **freelancing-ready automation script**, focusing on reliability, clarity, and extensibility.

This project is an enhanced and architecturally improved version of a basic price tracker, built to demonstrate real-world scraping design rather than one-off scripts.

---
## 📦 Project Overview

**Price Monitor** automatically checks product prices from multiple websites, stores historical prices in CSV format, and reports price drops via console alerts. The system is fully configuration-driven and can scale from a few products to thousands without changing core logic.

The project emphasizes:

- Clean separation of concerns

- Multi-site support

- Safe error handling

- Cron / scheduler-friendly execution
---
## ✨ Key Features

- Multi-site price tracking

- CSV-driven product input (no hardcoding)

- Historical price storage in CSV

- Console-based price drop alerts

- Modular scraper architecture (easy to add new sites)

- Graceful handling of HTTP/network errors

- External scheduling support (cron / Task Scheduler)
---
## 🧠 Project Architecture

- The system is divided into clear layers:

- Configuration Layer – Site-specific selectors stored in JSON

- Scraper Layer – One scraper class per site

- Core Logic Layer – Shared fetching and parsing logic

- Data Layer – CSV-based persistence

- Orchestration Layer – Main execution flow

- This design avoids hardcoding and allows easy extension without touching existing logic.
---

## 📁 Folder Structure
```
price-monitor/
│
├── main.py
│
├── config/
│ ├── sites.json           # Site selectors & metadata
│ └── sites.py             # JSON loader
│
├── scraper/
│ ├── base_scraper.py      # Shared scraping logic
│ ├── site_a.py            # Site A scraper
│ └── site_b.py            # Site B scraper
│
├── utils/
│ └── csv_handler.py       # CSV read/write utilities
│
├── data/
│ ├── products.csv         # Input products
│ └── price_history.csv    # Stored price history
│
└── README.md
```
---
## 🔄 How It Works (Execution Flow)

- Load products from products.csv

- Load site configurations from sites.json

- Select the appropriate scraper for each product

- Fetch product page

- Extract and clean price using scraper

- Store price with timestamp in price_history.csv

- Compare with last stored price

- Print console alert if price drops

 The script continues execution even if one product or site fails.

---
## 🏗 Scraper Architecture (CRITICAL)

- base_scraper.py

  - Defines shared scraping workflow:

    - fetch_page(url)
    - extract_price(html, selector, attribute)
    - clean_price(raw_price)
    - get_price(url, selector, attribute)

  - Parsing is centralized and reused via extract_price()

- site_a.py / site_b.py

  - Provide site-specific selectors
  - No scraping logic duplication
  - Only configuration differences

👉 This design keeps parsing consistent and makes adding new sites trivial.

---

- main.py

  - Execution Steps (LOCKED)

  - Load products.csv

  - For each product:

  - Fetch page

  - Extract price

  - Validate price

  - Compare with last known price

  - Append result to price_history.csv

  - Print console summary

  - print errors, skip failures

---
## 🛠 Installation & Setup

### Clone the repository
Clone or download the project, then navigate into the folder

```bash
git clone  https://github.com/kency07/price-monitor.git
cd  price-monitor
```
### Create and activate a virtual environment

```bash 
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Requirements

- Python 3.10+

- Internet connection

### Install Dependencies
```bash
pip install requests beautifulsoup4
```
---
## ⚙ Configuration
```
products.csv
product_id,product_name,site,product_url,target_price
101,iPhone 14,site_a,https://example.com/product/iphone14,55000
102,Samsung Galaxy S23,site_b,https://example.com/product/s23,50000
```
```
sites.json
{
  "site_a": {
    "name": "Example Store A",
    "currency": "INR",
    "price_selector": ".price",
    "price_attribute": null
  },
  "site_b": {
    "name": "Example Store B",
    "currency": "INR",
    "price_selector": "span.product-price",
    "price_attribute": null
  }
}
```
Example URLs are placeholders and intentionally non-functional

---
## ▶ Running the Script
```bash
python main.py
```
**Example Output**
```
[ERROR] Failed to fetch price for product 101
[ERROR] Failed to fetch price for product 102
```
(Errors are expected when using placeholder URLs.)

---
## 📥 Input Format — products.csv

```
product_id,product_name,site,product_url,target_price
101,Sample Product A,site_a,https://example.com/product/a,55000
102,Sample Product B,site_b,https://example.com/product/b,50000


```
Sample CSV files are included for reference. Replace them with your own data when running the script.

---

## 📤 Output Format — price_history.csv

```
timestamp,product_id,price
2026-01-04 10:30,101,54999
```
---
## 🖥 Console Output (Minimal but Clear)

Example:

```
[drop] Product 101: 54999 | 55000-> 54999
[ERROR] Failed to fetch price for product 102
```
- Currency symbols are intentionally omitted
- Output is minimal and cron-friendly

---
## ⚠ Error Handling Rules

- Network or HTTP errors → printed and skipped
- Parsing failures → skipped safely
- Missing price → skipped
- CSV read/write errors → raise exception

Reliability is prioritized over perfection.

---
## ⚠ Limitations

- Uses placeholder URLs only

- No JavaScript-rendered pages

- No proxy or user-agent rotation

- No email or messaging alerts

- CSV storage only (no database yet)

- These limitations are intentional to keep the project clean and focused.
---
## 🔮 Future Improvements

- SQLite / database storage

- Email or Telegram alerts

- Async scraping (Playwright / asyncio)

- Retry and backoff strategies

- Support for JavaScript-heavy sites

- Currency normalization
---
## 🧰 Technology Stack

**Language:** Python

**HTTP:** requests

**Parsing:** BeautifulSoup

**Storage:** CSV

**Scheduling:** External (cron / Task Scheduler)

**Alerts:** Console-based only

---

## 🎯 Supported Scope

```
Products: 1–750 (CSV driven, scalable by design)
Execution: CLI (cron / scheduler friendly)
```
---
## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
👨‍💻 Author

Built as a freelancing portfolio project to demonstrate:

Web scraping fundamentals

Clean Python architecture

Automation-ready scripting

⭐ If you find this project useful, feel free to star the repository.

---


