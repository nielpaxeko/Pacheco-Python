import datetime as dt
import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()


TOKEN = os.getenv("USER_TOKEN")
USERNAME =  os.getenv("USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")
graph_url = "https://pixe.la/v1/users/nielpaxeko/graphs/graph1"
pixela_endpoint = "https://pixe.la/v1/users"

# Create User, code not needed anymore
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text);

# Create graph code
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "lingvoj",
#     "unit": "minutes",
#     "type": "int",
#     "color": "shibafu",
   
# }
headers = {
         "X-USER-TOKEN": TOKEN
}
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Post a value to my graph
pixel_creation_endpoint = f"{"https://pixe.la/v1/users"}/{USERNAME}/graphs/{GRAPH_ID}"
TODAY = dt.date.today().strftime('%Y%m%d')
print(f"Today is: {TODAY}")
pixel_data = {
    "date": TODAY,
    "quantity": input("How many minutes did you study today? "),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)