# Day 32 Notes - Python SMTP (Simple Mail Transfer Protocol) and Datetime Module

# 1 - Send emails through python
# from email import message
# import smtplib

# my_email = "unknownpacha@gmail.com"
# pword = "aphlkbumqldntdcp"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = my_email, password = pword)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="edpvpro@hotmail.com",
#         msg= "Subject: Testing\n\nThis is the body of my email"
#     )
    
# Datetime module
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
print(day)

birthday = dt.datetime(year=2001, month=10, day=23)
print(birthday)

