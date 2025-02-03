import requests
import datetime as dt
from datetime import timezone
import time
import smtplib

# My Location
MY_LAT = 40.712776
MY_LONG = -74.005974
MY_POSITION = (MY_LAT, MY_LONG)

# Check ISS position through public API request
def ISS():
    print(f"The position of the ISS is {iss_position}, your position is {MY_POSITION}")
    print(f"The sun rises at {sunrise}")
    print(f"The sun sets at {sunset}")
    print(f"It is currently {now}")
    lat_condition = MY_LAT - 5.0 <= iss_latitude <= MY_LAT + 5.0
    long_condition = MY_LONG - 5.0 <= iss_longitude <= MY_LONG + 5.0
    sunset_condition = now >= sunset or now <=sunrise
    if lat_condition and long_condition and sunset_condition:
        print("LOOK UP!")
        lookUp()
    else:
        print("Don't even bother....")
        
def lookUp():
    my_email = "unknownpacha@gmail.com"
    pword = "aphlkbumqldntdcp"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = pword)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="edpvpro@hotmail.com",
            msg= "Subject: Look Up!!!\n\nThe ISS is right above you!!!"
        )

# get what's inside
response = requests.get(url='http://api.open-notify.org/iss-now.json')
# Check status
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_position = (iss_latitude, iss_longitude)

location_parameter ={
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted':0
}
sunrise_sunset_api = 'https://api.sunrise-sunset.org/json'
sun_response = requests.get(url = sunrise_sunset_api, params=location_parameter)
sun_response.raise_for_status()
print(sun_response.json())
sunrise = int(sun_response.json()['results']['sunrise'].split("T")[-1].split(":")[0])
sunset = int(sun_response.json()['results']['sunset'].split("T")[-1].split(":")[0])
now = dt.datetime.now(timezone.utc).hour

while True:
    ISS()
    time.sleep(60)
    