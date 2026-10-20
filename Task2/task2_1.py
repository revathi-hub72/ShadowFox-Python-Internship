
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")

    print("WEB SCRAPER - SHADOWFOX TASK 2")
    print("-" * 40)

    for number, book in enumerate(books, start=1):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").get_text(strip=True)

        print(f"{number}. Book: {title}")
        print(f"   Price: {price}")
        print()

    print("Total books found:", len(books))

except requests.RequestException as error:
    print("Unable to access the website.")
    print("Error:", error)
