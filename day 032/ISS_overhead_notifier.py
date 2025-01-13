#if the ISS is close to my current position
#and it is currently dark
#then send me an to tell me to look up 
# Bonus: run the code every 60 seconds

import requests
import smtplib
import datetime




MY_LATTITUDE = -17.820950
MY_LONGITUDE = 31.038160


#check if the iss is overhead
def is_iss_overhead():
        
    ISS_URL = 'http://api.open-notify.org/iss-now.json'

    response = requests.get(ISS_URL)
    response.raise_for_status()

    data = response.json()
    ISS_lattitude = data['iss_position']['latitude']
    ISS_longitude = data['iss_position']['longitude']
        
        
    if MY_LATTITUDE == ISS_lattitude and MY_LONGITUDE == ISS_longitude:
        return True
        
    
    
    
#check if its night time 
def  is_it_nighttime():
    parameters = {
        'lat': MY_LATTITUDE,
        'lng': MY_LONGITUDE,
        'formatted': 0
    }
    
    response = requests.get('https://api.sunrise-sunset.org/json', params= parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now().hour
    if time_now >= sunset and time_now <= sunrise:
        return True
        
    
    
    

my_email = 'fmudzungayiri97@gmail.com'
my_password = 'less secure password'

    
def send_email(message):
    
    if is_iss_overhead() and is_it_nighttime():
            
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
        
        

email_message = f"Subject: ISS Position \n\n Hey \n You look up now, the ISS is now above you."
send_email(message = email_message)