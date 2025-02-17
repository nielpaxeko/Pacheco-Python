from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# This code is necessary to keep chrome driver open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Instantiate driver and go to webpage
driver = webdriver.Chrome(options=chrome_options)
URL = "https://orteil.dashnet.org/cookieclicker/"
driver.get(URL)


def get_cookies():
    """Return amount of user cookies"""
    cookies = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0])
    print(cookies)
    return cookies

def buy_upgrade(products):
    cookies = get_cookies()
    highest_affordable_product = ""
    highest_affordable_price = 0
    for product, value in products.items():
        price = int(value["price"])
        id = value["id"]
        print(f"Price of {product} ({id}) = {price}")
        if price > highest_affordable_price and price <= cookies:
            highest_affordable_product = id
            highest_affordable_price = price  # Update the highest price found
    # Buy upgrade if one was found
    if highest_affordable_product:
        upgrade = driver.find_element(by=By.ID, value=highest_affordable_product)
        upgrade.click()

def get_products():
    # Make a dictionary of all products
    products = driver.find_elements(By.CLASS_NAME, value="productName")
    price = driver.find_elements(By.CLASS_NAME, value="price")
    items = driver.find_elements(By.CSS_SELECTOR, value="#store div.unlocked")
    item_ids = [item.get_attribute("id") for item in items]
    # Each product has a price and an identifier for later use in upgrades
    product_list = {}
    for i in range(len(item_ids)):
        product_list[products[i].text] = {
            "price": price[i].text,
            "id": item_ids[i],
        }
    return product_list


def check_store():
    products = get_products()
    buy_upgrade(products)


time.sleep(5)

# Code for geting past language selection
try:
    lang_button = driver.find_element(By.ID, "langSelect-EN")
    lang_button.click()
    time.sleep(3)
except:
    print("Language selection skipped.")

# Click on cookie
cookie = driver.find_element(By.ID, "bigCookie")
start_time = time.time()
last_store_check = start_time
duration = 5 * 60  # Run for 5 minutes

while time.time() - start_time < duration:
    cookie.click()  # Click the cookie

    # Check store every 5 seconds
    if time.time() - last_store_check >= 5:
        check_store()
        last_store_check = time.time()

# driver.close()


