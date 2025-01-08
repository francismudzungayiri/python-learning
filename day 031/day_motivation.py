import datetime as dt
import smtplib
import os
import random


receiver_email = input('Enter the reciever gmail address \n')
subject = input('Enter email subject \n')

my_email = 'fmudzungayiri97@gmail.com'
password = 'phaqfsxcyrlnhhxk'


quotes = []

now = dt.datetime.now()
week_day = now.weekday()
week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday','Sunday'] 

if(week_days[week_day] == 'Wednesday'):
    with open(os.path.expanduser("/Users/mbuluundi/Desktop/python/day 031/quotes.txt"), 'r') as quotes_file:
        quotes = quotes_file.readlines()
        
        rand_quote = random.choice(quotes)
        message = f"Subject: {subject} \n\n {rand_quote}"
        
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls() #encrpyts our message making it secure 
        connection.login(
            user=my_email, 
            password = password
        )

        connection.sendmail(
            from_addr = my_email, 
            to_addrs = receiver_email, 
            msg = rand_quote
        )

else:
    print(f"Today is {week_days[week_day]}, no motivational quote to send.")
        