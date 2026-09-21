import random
from datetime import datetime
import pandas
import smtplib
import os
# Your email credentials
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
# Get today's month and day
today = datetime.now()
today_tuple = (today.month, today.day)

# Read birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (row["month"], row["day"]): row
    for index, row in data.iterrows()
}


# Check if today is someone's birthday
if today_tuple in birthdays_dict:
   birthday_person= birthdays_dict[today_tuple]
   file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

   with open(file_path) as letter_file:
        contents = letter_file.read()
        contents= contents.replace("[NAME]", birthday_person["name"])

    # Send email
   with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}")

