from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
import os
import time


class InstagramBot:    
    
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()
        self.MY_PHONE = os.getenv("MY_PHONE")
        self.MY_PASSWORD = os.getenv("MY_PASSWORD")
        self.TARGET = os.getenv("TARGET")
        
         # Get website
        # This code is necessary to keep chrome driver open
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # Instantiate driver and get webpage
        self.driver = webdriver.Chrome(options = chrome_options)
        self.login()
        
    def login(self):
        URL = "https://www.instagram.com"
        self.driver.get(URL)
        time.sleep(3)
        login_input = self.driver.find_element(By.XPATH, value = "//input[@name='username']")
        password_input = self.driver.find_element(By.XPATH, value = "//input[@name='password']")
        login_input.send_keys(self.MY_PHONE)
        password_input.send_keys(self.MY_PASSWORD)
        self.driver.find_element(By.XPATH, value = "//button[@type='submit']").click()
        time.sleep(5)
        save_login_prompt = self.driver.find_element(By.XPATH, value = "//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()
        
    def find_followers(self):
        self.driver.get(self.TARGET)
        time.sleep(2)
        # Locate and click on the "followers" link
        followers_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers/')]")
        followers_link.click()
        self.follow()
       

    def follow(self):
        # Find follow buttons and click on all of them
        time.sleep(3)
        follow_buttons = self.driver.find_elements(By.XPATH, '//div[text()="Follow"]')
        try:
            for button in follow_buttons:
                button.click()
                time.sleep(1.1)
        
        except ElementClickInterceptedException:
            pass
        

bot = InstagramBot()
bot.find_followers()