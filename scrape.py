import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Scrape first 3 pages of books.toscrape
BASE_URL = "https://books.toscrape.com/catalogue/page-"

all_books = []

for page in range(1, 4):
    url = f"{BASE_URL}{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()

        all_books.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    time.sleep(1)  # pause to avoid server issues

# Save raw data
books_df = pd.DataFrame(all_books)
books_df.to_csv("data/raw_books.csv", index=False)
print("Scraping completed ")
