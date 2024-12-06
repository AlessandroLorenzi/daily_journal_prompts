#!/usr/bin/env python3
import datetime
import smtplib
from email.mime.text import MIMEText
import os


EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

day_of_year = datetime.datetime.now().timetuple().tm_yday
with open("./prompts.txt", "r") as file:
    prompts = file.readlines()


def send_email(body):
    msg = MIMEText(body)
    msg["Subject"] = "📝 Prompt of the day 📝"
    msg["From"] = EMAIL_LOGIN
    msg["To"] = EMAIL_LOGIN

    with smtplib.SMTP_SSL("smtp.fastmail.com", 465) as server:
        server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        server.sendmail(EMAIL_LOGIN, EMAIL_LOGIN, msg.as_string())


prompt_of_the_day = prompts[day_of_year - 1].strip()
print(f"Prompt of the day: {prompt_of_the_day}")
send_email(prompt_of_the_day)
