import pandas as pd
import random as rand
import datetime as dt
import smtplib

list_of_quotes = {}
with open("quotes.txt") as quotes:
    for quote in quotes:
        new_quote = quote.split(" - ")
        list_of_quotes[new_quote[0].strip('"')] = new_quote[1].strip()
        
random_quote = rand.choice(list(list_of_quotes.items()))
print(random_quote)


my_email = "unknownpacha@gmail.com"
pword = "aphlkbumqldntdcp"
now = dt.datetime.now()

if now.weekday() == 6:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = pword)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="edpvpro@hotmail.com",
            msg= f"Subject: Testing\n\n{random_quote}"
        )
    print("Message sent successfully")
else:
    print("Today is not sunday")