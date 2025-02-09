from flask import Flask, render_template, request
import smtplib
import os
from dotenv import load_dotenv

app = Flask(__name__)





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
    

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('name')
        useremail = request.form.get('email')
        subject = request.form.get('subject')
        comment = request.form.get('comment')
        
        send_email(username, useremail, subject,comment)
        
        
        
    return render_template('index.html')



if __name__ == 'main':
    app.run(debug = True)

