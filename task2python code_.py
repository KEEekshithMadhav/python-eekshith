import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 12):
    url = f"https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers"
    }
    
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"Failed to retrieve the page {i}")
        continue

    soup = BeautifulSoup(r.text, "html.parser")
    boxes = soup.find_all("div", class_="DOjaWF gdgoEp")

    for box in boxes:
        names = box.find_all("div", class_="KzDlHZ")
        prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
        descs = box.find_all("div", class_="_6NESgJ")  # Updated class for description
        reviews = box.find_all("div", class_="XQDdHH")

        max_len = max(len(names), len(prices), len(descs), len(reviews))

        for j in range(max_len):
            if j < len(names):
                Product_name.append(names[j].text)
            else:
                Product_name.append(None)

            if j < len(prices):
                Prices.append(prices[j].text)
            else:
                Prices.append(None)

            if j < len(descs):
                Description.append(descs[j].text)
            else:
                Description.append(None)

            if j < len(reviews):
                Reviews.append(reviews[j].text)
            else:
                Reviews.append(None)
    
    # Delay before the next request to avoid overloading the server
    time.sleep(5)

# Debugging output to check the extracted data
print("Product Names:", Product_name)
print("Prices:", Prices)
print("Descriptions:", Description)
print("Reviews:", Reviews)

# Creating DataFrame
df = pd.DataFrame({
    "Product_name": Product_name,
    "Prices": Prices,
    "Description": Description,
    "Reviews": Reviews
})

#print(df)

df.to_csv("D:/python intern/flipkart_moblies_under_50000.csv")
