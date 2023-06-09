import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from flask import Flask

app = Flask(__name__)


# Send a GET request to the URL
url = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all common elements using BeautifulSoup
elements_bs = soup.find_all("div", class_="primary")

# Use Selenium to render the page with JavaScript
driver_path = r"C:\Users\user\Downloads\chromedriver_win32"
 
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver
driver.get(url)


# Find all instances of the div with class 'primary' using Selenium
elements_selenium = driver.find_elements(By.CSS_SELECTOR, "div.primary")

# Print the contents of the elements found by BeautifulSoup
for element_bs in elements_bs:
    print(element_bs.text)

# Print the contents of the elements found by Selenium
for element_selenium in elements_selenium:
    print(element_selenium.text)
    
if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)

# Close the web driver
driver.quit()
