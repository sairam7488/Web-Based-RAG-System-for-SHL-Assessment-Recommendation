# scraper/scrape_shl.py

import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.shl.com"

CATEGORY_URLS = [
    "https://www.shl.com/solutions/products/ability-tests/",
    "https://www.shl.com/solutions/products/personality-questionnaires/",
    "https://www.shl.com/solutions/products/behavioral-assessments/",
    "https://www.shl.com/solutions/products/cognitive-tests/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

assessments = []
seen = set()

for url in CATEGORY_URLS:
    print(f"Scraping category: {url}")
    response = requests.get(url, headers=HEADERS, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if not href.startswith("/products/"):
            continue

        full_url = BASE_URL + href
        if full_url in seen:
            continue

        name = a.get_text(strip=True)
        if not name or len(name) < 4:
            continue

        seen.add(full_url)

        assessments.append({
            "name": name,
            "url": full_url,
            "description": f"{name} assessment",
            "test_type": ["Ability / Personality"],
            "duration": 15,
            "adaptive_support": "Yes",
            "remote_support": "Yes"
        })

print("\n===================================")
print("Total assessments scraped:", len(assessments))
print("===================================\n")

with open("data/raw/shl_catalog.json", "w", encoding="utf-8") as f:
    json.dump(assessments, f, indent=2)

print("Saved to data/raw/shl_catalog.json")