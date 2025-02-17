from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# This code is necessary to keep chrome driver open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Instantiate driver and get webpage
driver = webdriver.Chrome(options = chrome_options)
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)

# Click on link
articles = driver.find_element(By.XPATH, value = '//*[@id="articlecount"]/ul/li[2]/a[1]').text
# articles.click() # this is one method

# This is another method to achieve the same
# portals = driver.find_element(By.LINK_TEXT, value = "Content portals") # Value is = text on the link
# articles.click() # this is the other method

# Find the search <input> by name AND search wikipedia for anything I like
search = driver.find_element(By.Name, value = "search")
search.send_keys("Python", Keys.ENTER)

print(articles)
driver.close()