##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the
# [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import smtplib

gmail_email = "testjamjam.perey@gmail.com"  # your personal email that will be sending emails
password = "hmrjihsqpxddhonn" # changed for security - code will not work due to this
yahoo_app_pw = ""
yahoo_email = "jamjam.perey@yahoo.com"
yahoo_smtp = "smtp.mail.yahoo.com"
gmail_smtp = "smtp.gmail.com"

csv_data = pandas.read_csv("birthdays.csv")
csv_list = csv_data.values.tolist()  # contains contact info in list form
csv_name = csv_list[0][0]
csv_email = csv_list[0][1]
csv_year = csv_list[0][2]
csv_month = csv_list[0][3]
csv_day = csv_list[0][4]

current_date = dt.datetime.now()
current_day = current_date.weekday()
current_month = current_date.month

if current_day == csv_day and current_month == csv_month:
    letter_choice = random.randint(1, 3)
    with open(file=f"letter_templates/letter_{letter_choice}.txt", mode="r") as file:
        files_contents = file.read()

finished_file = files_contents.replace("[NAME]", csv_name)

print(finished_file)

connection = smtplib.SMTP(gmail_smtp, port=587)
connection.starttls()
connection.login(user=gmail_email, password=password)
connection.sendmail(from_addr=gmail_email, to_addrs=yahoo_email, msg=f"Subject: Happy Birthday!\n\n{finished_file}")
