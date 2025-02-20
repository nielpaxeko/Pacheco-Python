from turtle import down
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time


class InternetSpeedTwitterBot:    
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()
        self.MY_EMAIL = os.getenv("MY_EMAIL")
        self.MY_PASSWORD = os.getenv("MY_PASSWORD")
        self.MY_USERNAME = os.getenv("MY_USERNAME")
        self.PROMISED_DOWN = 150
        self.PROMISED_UP = 10
        self.down = 0
        self.up = 0
        
        # Get website
        # This code is necessary to keep chrome driver open
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # Instantiate driver and get webpage
        self.driver = webdriver.Chrome(options = chrome_options)
        # Get speeds
        self.get_internet_speed()
        # Login
        self.login()
        time.sleep(3)
        self.tweet_at_provider()
    
    def login(self):
        URL = "https://x.com/i/flow/login"
        self.driver.get(URL)
        time.sleep(3)
        login_input = self.driver.find_element(By.XPATH, value = "//input[@name='text']")
        login_input.send_keys(self.MY_EMAIL)
        self.driver.find_element(By.XPATH,  value = "//span[text()='Next']/ancestor::button").click()        
        time.sleep(2)
        username_input = self.driver.find_element(By.XPATH, value = "//input[@name='text']")
        username_input.send_keys(self.MY_USERNAME)
        self.driver.find_element(By.XPATH,  value = "//span[text()='Next']/ancestor::button").click()
        time.sleep(2) 
        password_input = self.driver.find_element(By.XPATH, value = "//input[@name='password']")
        password_input.send_keys(self.MY_PASSWORD)
        self.driver.find_element(By.XPATH,  value = "//span[text()='Log in']/ancestor::button").click()
    
    def get_internet_speed(self):
        # Load site
        URL = "https://www.speedtest.net"
        self.driver.get(URL)
        time.sleep(2)
        start = self.driver.find_element(By.CLASS_NAME, value = "js-start-test").click()
        # Wait
        time.sleep(40)
        speeds = self.driver.find_elements(By.CLASS_NAME, value = "result-data-value")
        self.down = speeds[0].text
        self.up = speeds[1].text
        print(f"Download speed = {self.down}")
        print(f"Upload speed = {self.up}")
    
    def tweet_at_provider(self):
        # Create tweet
        tweet_compose = self.driver.find_element(By.XPATH, value = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {self.PROMISED_DOWN}down/{self.PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        # Post Tweet
        # tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        # tweet_button.click()

bot = InternetSpeedTwitterBot()