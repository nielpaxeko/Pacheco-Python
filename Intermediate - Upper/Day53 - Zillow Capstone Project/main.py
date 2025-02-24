from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
import os
import re
import time

class PropertySearcher():
    
    def __init__(self):
        load_dotenv()
        self.GOOGLE_FORM = os.getenv("GOOGLE_FORM")
        # Get website
        # This code is necessary to keep chrome driver open
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # Instantiate driver and get webpage
        self.driver = webdriver.Chrome(options = chrome_options)
        URL = "https://appbrewery.github.io/Zillow-Clone/"
        self.driver.get(URL)
        time.sleep(4)
        self.getProperties()
    
    def getProperties(self):
        addresses = self.driver.find_elements(By.XPATH, "//address[@data-test='property-card-addr']")
        prices = self.driver.find_elements(By.XPATH, "//span[@data-test='property-card-price']")
        links = self.driver.find_elements(By.XPATH, "//a[@data-test='property-card-link']")
        link_ids = [link.get_attribute("href") for link in links]
        properties = {}
        for idx in range(len(addresses)):
            properties[f"Property NO.{idx+1}"] = {
                "address": addresses[idx].text,
                "price": re.split(r"[/+ ]", prices[idx].text)[0],
                "link": link_ids[idx],
            }
        self.fill_form(properties)
           
    def fill_form(self, properties):
        # Get form webpage
        self.driver.get(self.GOOGLE_FORM)
        time.sleep(2)
        for property in properties.values():
            # Get inputs
            inputs = self.driver.find_elements(By.XPATH, value = "//input[@type='text']")
            address_input = inputs[0]
            price_input = inputs[1]
            link_input = inputs[2]
            submit_btn = self.driver.find_element(By.XPATH, value = "//div[@role='button']")
            # Submit form
            address_input.send_keys(property["address"])
            price_input.send_keys(property["price"])
            link_input.send_keys(property["link"])
            submit_btn.click()
            time.sleep(1)
            self.driver.get(self.GOOGLE_FORM)
            time.sleep(1)

searcher = PropertySearcher()

