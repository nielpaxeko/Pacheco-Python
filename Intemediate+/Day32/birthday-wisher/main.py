##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas as pd
import smtplib
birthday_list = []
my_email = "unknownpacha@gmail.com"
pword = "aphlkbumqldntdcp"


# 1. Read the birthdays.csv
birthday_file = pd.read_csv("birthday-wisher/birthdays.csv")
bday_df = pd.DataFrame(birthday_file.to_dict())

# 2. Check if today matches a birthday in the birthdays.csv
def check_date():
    now = dt.datetime.now()
    month = now.month
    day = now.day
    found_person = False
    for idx, row in bday_df.iterrows():
        if row["month"] == month and row["day"] == day:
            print(f"It's {row["name"]}'s birthday.")
            birthday_person = row
            birthday_list.append(birthday_person)
            found_person = True
    return found_person        

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if check_date():
    for person in birthday_list:
        random_idx = random.randint(1,3)
        with open(f"birthday-wisher/letter_templates/letter_{random_idx}.txt", "r") as letter:
            letter_contents = letter.read()
            letter_contents = letter_contents.replace("[NAME]", person["name"])
            print(letter_contents)
            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user = my_email, password = pword)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=person["email"],
                        msg= f"Subject: Happy birthday!\n\n{letter_contents}"
                    )
else:
    print("It's nobody's birthday today...")
    


