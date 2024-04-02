import smtplib
import os


class EmailService:

    def __init__(self):
        self.EMAIL_ACCOUNT = os.environ['EMAIL_ACCOUNT']
        self.EMAIL_APP_PWD = os.environ['EMAIL_APP_PWD']

    def send_email(self, recipient, subject, body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.EMAIL_ACCOUNT, self.EMAIL_APP_PWD)
            connection.sendmail(self.EMAIL_ACCOUNT, recipient, f"Subject:{subject}\n\n{body}")
