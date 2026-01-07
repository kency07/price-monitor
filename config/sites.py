import json
from pathlib import Path

CONFIG_PATH = Path("config/sites.json")

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    SITE_CONFIG = json.load(f) 