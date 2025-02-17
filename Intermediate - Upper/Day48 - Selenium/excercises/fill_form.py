from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# This code is necessary to keep chrome driver open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Instantiate driver and go to webpage
driver = webdriver.Chrome(options = chrome_options)
URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

# Get form
first_name = driver.find_element(By.NAME, value = "fName")
last_name = driver.find_element(By.NAME, value = "lName")
email = driver.find_element(By.NAME, value = "email")

# Fill form
first_name.send_keys("Edgar")
last_name.send_keys("Pacheco")
email.send_keys("nielpaxekin@gmail.com")

button = driver.find_element(By.XPATH, value = '/html/body/form/button')
button.click()

# driver.close()