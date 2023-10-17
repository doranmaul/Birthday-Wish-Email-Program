import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "input email here"
PASSWORD = "input app password here"  # Generate app password, 2-step verify
TOTAL_NUMBER_LETTERS = 3  # Total number of letters here

date = dt.datetime
today = date.today()
month = today.month
day = today.day

pandas_csv = pandas.read_csv("birthdays.csv")
birthday_s = pandas.DataFrame(pandas_csv)
birthday_dict = birthday_s.to_dict(orient="records")

for items in birthday_dict:
    if items["month"] == month and items["day"] == day:
        with open(f"../input-letter-file-paths-here/letter_{random.randint(1, TOTAL_NUMBER_LETTERS)}.txt") as current_letter:
            letter = current_letter.read()
            final_letter = letter.replace("[NAME]", items["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=f"{items['email']}",
                                msg=f"Subject:Happy Birthday {items['name']}\n\n{final_letter}")





