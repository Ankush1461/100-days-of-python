import smtplib

from twilio.rest import Client

TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH_TOKEN = "AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = "VIRTUAL_NUMBER"
TWILIO_VERIFIED_NUMBER = "TWILIO_VERIFIED_NUMBER"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
# MailID and Password
MY_EMAIL = "xyz@gmail.com"
MY_PASSWORD = "xyz@123"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
