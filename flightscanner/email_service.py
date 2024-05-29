import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailService:

    def __init__(self):
        self.EMAIL_ACCOUNT = os.environ["EMAIL_ACCOUNT"]
        self.EMAIL_APP_PWD = os.environ["EMAIL_APP_PWD"]

    def send_email(self, subject, body):
        receiver_emails = [self.EMAIL_ACCOUNT]

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = self.EMAIL_ACCOUNT
        msg["To"] = ", ".join(receiver_emails)

        # Attach HTML message
        html_part = MIMEText(body, "html")
        msg.attach(html_part)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.EMAIL_ACCOUNT, self.EMAIL_APP_PWD)
            connection.sendmail(self.EMAIL_ACCOUNT, receiver_emails, msg.as_string())
