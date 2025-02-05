import requests
import smtplib

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
my_email = os.getenv("MY_EMAIL")
pword = os.getenv("EMAIL_PASSWORD")
api_key = os.getenv("API_KEY")

# API CALL
parameters = {
    # Tokyo coordinates
    "lat": "35.689487",
    "lon": "139.691711",
    "appid": api_key,
    "cnt": 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast??", params=parameters)
response.raise_for_status()
weather_data = response.json()


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# Send Message
if will_rain:
    message = 'Subject:Hello there, Weather Alert\n\nIt will rain today, bring an umbrella!'
else:
    message = "Subject:Hello there, Weather Alert\n\nIt might not rain today, but bring an umbrella just in case!"
    
with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = pword)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="edpvpro@hotmail.com",
            msg= f"{message}"
        )
        print("Message sent successfully")
    

