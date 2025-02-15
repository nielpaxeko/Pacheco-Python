from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import smtplib
import os

def send_email(name, price):
        """Sends email notifying user of price drop"""
        # Load environment variables from the .env file
        load_dotenv()
        SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
        EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
        MESSAGE = f"Subject: Price Drop\n\n{name} is now ${price}."
        # Send Email
        print(MESSAGE)
        with smtplib.SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user = EMAIL_ADDRESS, password = EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_ADDRESS,
                to_addrs="edpvpro@hotmail.com",
                msg= MESSAGE.encode('utf-8')
            )
            print("Message sent successfully")

def find_price():
    """Finds Price of Instant Pot and returns True if value is below set amount of 100 USD"""
    URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
    # Full headers would look like this
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
        "Dnt": "1",
        "Priority": "u=1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Sec-Gpc": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    }
    # Get webpage from URL
    response = requests.get(URL, headers=header)
    response.raise_for_status()
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    try:
        name = soup.find(id="productTitle").getText().strip()
        whole = soup.find(name="span", class_="a-price-whole").getText()
        fraction =  soup.find(name="span", class_="a-price-fraction").getText()
        price = float(whole + fraction)
        print(f"Current price of item is: {price}")
        # Send email if price below 100 USD
        if price < 100.00:
            send_email(name, price)
            return price < 100.00
        else:
            print("Item price is not below set amount of 100 USD")
            return False
    except AttributeError as error:
        print("Value not Found")
            
find_price()