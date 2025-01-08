import smtplib

receiver_email = input('Enter the reciever gmail address \n')
subject = input('Enter email subject \n')
message = input('Enter your message \n')

my_email = 'fmudzungayiri97@gmail.com'
password = 'less secure password'


text = f"Subject:{subject} \n\n {message}"

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls() #encrpyts our message making it secure 
    connection.login(
        user=my_email, 
        password = password
    )

    connection.sendmail(
        from_addr = my_email, 
        to_addrs = receiver_email, 
        msg = text
    )


#using with keyword provides an automatic close after its use. so you will have to skip this line below
#connection.close()
