import smtplib
from email.mime.text import MIMEText
import os


EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_LOGIN
    msg["To"] = EMAIL_LOGIN

    with smtplib.SMTP_SSL("smtp.fastmail.com", 465) as server:
        server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        server.sendmail(EMAIL_LOGIN, EMAIL_LOGIN, msg.as_string())
