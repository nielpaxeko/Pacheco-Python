# Advanced Web Scraping: Selenium Webdriver -> One of the most well-known pentesting tool, selenium can automate the browser
from selenium import webdriver 
from selenium.webdriver.common.by import By

# This code is necessary to keep chrome driver open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Instantiate driver and get webpage
driver = webdriver.Chrome(options = chrome_options)
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
driver.get(URL)

# Find element by class
whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"Full price is: {whole.text}.{fraction.text}")

# Find elements by name
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# Find elements by id
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# Find elements by css selector
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

# Find elements by xpath
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Close driver options
driver.close()  # this closes the active tab
# driver.quit() # this closes the entire browser

