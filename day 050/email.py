import smtplib 
from dotenv import load_dotenv
import os

def send_email(name,email_receiver, subject, message):
    load_dotenv()
    SENDER_EMAIL = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD =  os.getenv('YAHOO_APP_PASSWPORD')
    
    with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
        connection.starttls()
        connection.login(
            email = SENDER_EMAIL,
            password= EMAIL_PASSWORD
        )
        print('USER LOGIN SUCCESSFULL')
        
        text_message = f'Subject {subject}/n/n Hi Mr {name}/n/n {message}'
        connection.sendmail(
            from_addr= SENDER_EMAIL, 
            to_addrs= email_receiver,
            msg= text_message
        )

        print('EMAIL SEND SUCCESSFULLY.')
    