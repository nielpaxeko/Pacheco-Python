from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/instant_pot/"

# Get webpage from URL
response = requests.get(URL)
response.raise_for_status()
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

def find_price():
    pass