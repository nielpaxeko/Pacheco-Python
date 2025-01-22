import requests
import smtplib

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")
AV_API_KEY = os.getenv("AV_API_KEY")

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
AV_URL = 'https://www.alphavantage.co/query?'
AV_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "compact",
    "apikey": AV_API_KEY
}

# Get close values
response = requests.get(AV_URL, params=AV_PARAMS)
av_data = response.json()

ayer_close = round(float(list(av_data["Time Series (Daily)"].values())[0]["4. close"]))
anteayer_close = round(float(list(av_data["Time Series (Daily)"].values())[1]["4. close"]))
print(ayer_close)
print(anteayer_close)

# Check for major change
major_change = False
difference = round(((ayer_close - anteayer_close) * 100) / anteayer_close)
print(f"Difference: {difference}")
if (abs(difference) > 5):
    major_change = True

if major_change:
    NEWS_URL = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    NEWS_PARAMS = {
        "q": COMPANY_NAME,
        "searchIn": "description",
        "language": "en",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY,
    }


    news_request = requests.get(NEWS_URL, params=NEWS_PARAMS)
    news_request.raise_for_status()
    news_data = news_request.json()

    # Send email reporting major change and latest news on the company
    for i in range(3):
        company = f"{STOCK}: {str(difference)}%"
        headline = "Headline: " + news_data["articles"][i]["title"]
        desc = "Brief: " + news_data["articles"][i]["description"]
        message = f"Subject: Stock Update: {STOCK}\n\n{company}\n{headline}\n{desc}"
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user = MY_EMAIL, password = PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="edpvpro@hotmail.com",
                    msg= message
                )
                print("Message sent successfully")
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
        
    

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


