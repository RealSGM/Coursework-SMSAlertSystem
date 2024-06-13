from email.message import EmailMessage
import smtplib, ssl, os
from dotenv import load_dotenv

load_dotenv()

## Global Variables
sender_email = 'pu.ngaol.weather.alert@gmail.com'
sender_password = os.getenv('GOOGLE_PASSKEY')

def send_email(receiver_email, subject, body):
    #print(f"Sending email to {receiver_email}")
    em = EmailMessage()
    em["From"] = sender_email
    em["To"] = receiver_email
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, em.as_string())