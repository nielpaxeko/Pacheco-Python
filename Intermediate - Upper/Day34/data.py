import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 22
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status() # Check for errors
data = response.json()
question_data = data["results"]