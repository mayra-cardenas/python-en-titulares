import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://blog.python.org/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

items = []

posts = soup.find_all("h3", class_="post-title")

for post in posts[:25]:
    a = post.find("a")
    items.append({
        "titulo": a.get_text(strip=True),
        "link": a["href"]
    })

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

df = pd.DataFrame(items)
df.to_csv(os.path.join(DATA_DIR, "raw.csv"), index=False)

print(f"Scraping completo: {len(df)} posts guardados ✔️")