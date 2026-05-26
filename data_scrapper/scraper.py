import requests
from bs4 import BeautifulSoup
import csv
import os

#website url 
URL = "https://books.toscrape.com"

def get_webpage():
    """
    sends request to website and gets HTML content
    """
    try:
        response = requests.get(URL)
        #check if request was successful
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as error:
        print(f"Error fetching website: {error}")
        return None
    
def parse_data(html):
    """
    extract book information from HTML
    """

    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("article", class_ = "product_pod")

    scraped_data = []
    for book in books:
        #book title
        title = book.h3.a["title"]

        # book price
        price = book.find("p", class_ = "price_color").text
        #book rating
        rating = book.find("p")["class"][1]
        # store data in dictionary
        scraped_data.append({
            'Title' : title,
            'Price' : price,
            'Rating' : rating
        })
    return scraped_data

def save_to_csv(data):
    """
    saves scraped data  into CSv file 
    """
    try:
        #get the folder where scraper.py is located
        current_folder = os.path.dirname(os.path.abspath(__file__))
        # create full path for books.csv
        csv_path = os.path.join(current_folder, "books.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["Title", "Price", "Rating"]
            )
            # writer colomns
            writer.writeheader()
            # writer rows
            writer.writerows(data)
        print("Data saved successfuly to books.csv")

    except Exception as error:
        print(f"error saving CSV file: {error}")

def main():
    print("starting web scrapper...........")
    html = get_webpage()
    if html:
        data = parse_data(html)
        if data:
            save_to_csv(data)
            print("\n scrapped book: ")

            for book in data:
                print(
                    f"Title: {book['Title']}\n"
                    f"Price: {book['Price']}\n"
                    f"Rating: {book['Rating']}\n"
                )
        else:
            print("NO data found")
    else:
        print("could not retrieve webpage")

if __name__ == "__main__":
    main()


