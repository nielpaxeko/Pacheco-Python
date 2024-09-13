import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("MY_EMAIL")
pword = os.getenv("EMAIL_PASSWORD")


class NotificationManager:
    def __init__(self):
        pass

    def send_email(self, message_body):
        my_email = os.getenv("MY_EMAIL")
        pword = os.getenv("EMAIL_PASSWORD")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=pword)

            connection.sendmail(
                from_addr=my_email,
                to_addrs="edpvpro@hotmail.com",
                msg=f"Subject:Flight Deal!\n\n{message_body}",
            )
            print("Message sent successfully")
