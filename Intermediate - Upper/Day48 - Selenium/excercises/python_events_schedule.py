from selenium import webdriver
from selenium.webdriver.common.by  import By


# This code is necessary to keep chrome driver open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Instantiate driver and get webpage
driver = webdriver.Chrome(options = chrome_options)
URL = "https://www.python.org/"
driver.get(URL)

# Get events and make a dictionary
event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li time")
events_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li a")
events = {}
print("Event List: \n")
for i in range(len(event_dates)):
    events[i+1] = {
        'date': event_dates[i].text,
        'name': events_names[i].text,
    }
    print(f"Date = {event_dates[0].text}")
    print(f"Event = {events_names[1].text}\n")
    
# print(event_list)
    
    
driver.close()  