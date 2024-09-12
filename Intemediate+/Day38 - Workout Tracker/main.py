import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# This program essentially asks the user what excercise they did on that day 
# It then adds the data as a new row to a google sheets using the sweety and nutrionix APIs 
# Load environment variables from the .env file
load_dotenv()
NUTRIONIX_APP_ID = os.getenv("NUTRIONIX_APP_ID")
NUTRIONIX_API_KEY = os.getenv("NUTRIONIX_API_KEY")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SWEETY_ENDPOINT = os.getenv("SWEETY_ENDPOINT")



# Constants
WEIGHT = 81
HEIGHT = 176
AGE = 22

query = input("Tell me what you excercise you did today: ")

nutrionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrionix_params = {
    "query": query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
nutrionix_headers = {
    "x-app-id": NUTRIONIX_APP_ID,
    "x-app-key": NUTRIONIX_API_KEY,
}

# Create nutrionix data from workout
response = requests.post(url=nutrionix_endpoint, json=nutrionix_params, headers=nutrionix_headers)
result = response.json()

# Add data to google sheets
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        SWEETY_ENDPOINT, 
        json=sheet_inputs, 
        auth=(
            USERNAME, 
            PASSWORD,
        )
    )


    print(sheet_response.text)