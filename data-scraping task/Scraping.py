import requests
from bs4 import BeautifulSoup

url = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all instances of the price element
prices = soup.find_all("div", class_="primary")

# Print the prices
for price in prices:
    print(price.text)

