from turtle import position
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException, ElementNotInteractableException
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os
import time
 # Load environment variables from the .env file
load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_PHONE = os.getenv("MY_PHONE")

# This code is necessary to keep chrome driver open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Instantiate driver and get webpage
driver = webdriver.Chrome(options = chrome_options)

def sign_in():
    # Go to job page
    URL = "https://www.linkedin.com/jobs/search/?currentJobId=4151454966&f_AL=true&f_E=2&geoId=90000070&keywords=%22python%20developer%22&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
    driver.get(URL)
    time.sleep(3)
    # Sign in redirect
    try:
        sign_in_redirect_btn = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
        sign_in_redirect_btn.click()
    except NoSuchElementException:
        print("Sign-in button not found.")
    except ElementClickInterceptedException:
        print("Could not interact with the sign-in button.")
    except ElementNotInteractableException:
        print(f"Unexpected error:")
        pass
   
    # Get sign in form
    time.sleep(2)
    try:
        email_field = driver.find_element(By.ID, "base-sign-in-modal_session_key")
        pw_field = driver.find_element(By.ID, "base-sign-in-modal_session_password")
        email_field.send_keys(MY_EMAIL)
        pw_field.send_keys(MY_PASSWORD)
    except NoSuchElementException:
        print("Email or password field not found.")
    # Attempt sign in
    time.sleep(2)
    try:
        sign_in_btn = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
        sign_in_btn.click()
    except NoSuchElementException:
        print("Sign-in button not found on the form.")
    except ElementClickInterceptedException:
        print("Sign-in button could not be clicked.")
    time.sleep(5)
    apply()

def apply():
    """Returns a pytho dictionary of all job positions found"""
    # NO. of results
    job_results = int(driver.find_element(By.XPATH, value = '//*[@id="main"]/div/div[2]/div[1]/header/div[1]/small').text.split(" ")[0])
    print(f"There are {job_results} jobs that match your search criteria. \n")
    # Get job applications
    company = driver.find_elements(By.CSS_SELECTOR, value = "a span strong")
    position = driver.find_elements(By.CLASS_NAME, value = "artdeco-entity-lockup__subtitle")
    location = driver.find_elements(By.CLASS_NAME, value = "artdeco-entity-lockup__caption")
    job_divs = driver.find_elements(By.CSS_SELECTOR, "div[data-job-id]")
    job_ids = [div.get_attribute("data-job-id") for div in job_divs]
    job_positions = {}
    for i in range(job_results):
        job_positions[f"Job Offer NO.{i+1}"] = {
            "company": company[i].text,
            "position": position[i].text,
            "location": location[i].text,
            "job_id": job_ids[i],
        }
    print(job_positions)
    submit(job_positions)
   
def submit(job_positions):
    # Apply to each job position
    number_of_applications = 0
    for offer, values in job_positions.items(): 
        job_id = values["job_id"]
        driver.find_element(By.CSS_SELECTOR, f"div[data-job-id='{job_id}']").click()
        time.sleep(1)
        try:
            driver.find_element(By.CSS_SELECTOR,
                                     '.jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary'
                                     '.ember-view').click()
            time.sleep(3)
        except NoSuchElementException:
            print(f"Easy Apply button not found for job {job_id}.")
            continue
            
        try:
            footer_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
            btn_label = footer_button.get_attribute("aria-label")
            print(f"Application button label = {btn_label}\n")
            if btn_label != "Submit your application":
                abort_application()
                time.sleep(2)
                print("Complex application, skipped.")
                continue
            else:
                footer_button.click()
                print("Submitting job application")
                number_of_applications+=1
                # Click Close Button
                close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
                close_button.click()
        except NoSuchElementException as e:
                print(f"Failed to apply for job {job_id}: {e}")
    print(f"Successfully applied to {number_of_applications} jobs applications")

def abort_application():
    # Click Close Button
    try:
        close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        # Click Discard Button
        discard_button = driver.find_elements(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[0]
        discard_button.click()
    except NoSuchElementException as e:
        print(f"Failed to abort application: {e}")

sign_in()

