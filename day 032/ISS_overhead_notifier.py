#if the ISS is close to my current position
#and it is currently dark
#then send me an to tell me to look up 
# Bonus: run the code every 60 seconds

import requests
import smtplib
import datetime




ISS_URL = 'http://api.open-notify.org/iss-now.json'

response = requests.get(ISS_URL)
response.raise_for_status()

data = response.json()
ISS_lattitude = data['iss_position']['latitude']
ISS_longitude = data['iss_position']['longitude']

MY_LATTITUDE = -17.820950
MY_LONGITUDE = 31.038160

my_email = 'fmudzungayiri97@gmail.com'
my_password = 'phaqfsxcyrlnhhxk'


message = f"Subject: ISS Position \n\n Hey \n You look up now, the ISS is now above you."

if MY_LATTITUDE == ISS_lattitude and MY_LONGITUDE == ISS_longitude:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(
            user = my_email,
            password = my_password
        )
        connection.sendmail(
            from_addr = my_email,
            to_addrs = 'francismudzungayiri@yahoo.com',
            msg = message
        )
        print('messsage send successfuly')
        
        
else:
    print('The ISS POSITION IS NOT NOWHERE NEAR YOU')
