import os 
import random 
import smtplib
import datetime as dt
import pandas as pd


now = dt.datetime.now()
now_month = now.month
now_day = now.day

my_email = 'fmudzungayiri97@gmail.com'
my_password = 'your_less_strict_passwod'

letters = ['letter_1.txt', 'letter_2.txt','letter_3.txt']
choosen_letter = random.choice(letters)

birthday_message = ''



df = pd.read_csv(os.path.expanduser('/Users/mbuluundi/Desktop/python/day 031/birthdays.csv'))
for index,row in df.iterrows():
    if row['month'] == now_month and row['day'] == now_day:
        
        with open(os.path.expanduser(f'/Users/mbuluundi/Desktop/python/day 031/letter_templates/{choosen_letter}'), 'r') as letter_file:
            row_content = letter_file.read()
            birthday_message = row_content.replace('[NAME]', row['name'])
        
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(
                user = my_email,
                password = my_password
            ) 
            connection.sendmail(
                from_addr = my_email,
                to_addrs = row['email'],
                msg = birthday_message
                
            )   
            
            
        print('Birthday message email send succeful.......')    
    
    else:
        print('NO BIRTHDAY EMAIL TO SEND TODAY')    

