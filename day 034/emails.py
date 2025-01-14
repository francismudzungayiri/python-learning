import smtplib

my_email = 'fmudzungayiri97@gmail.com'
password = 'less secure pass'


smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()

smtp.starttls()
smtp.login(my_email, password = password)

smtp.sendmail(
    to_addrs = 'francismudzungayiri@yahoo.com', 
    from_addr=my_email, 
    msg = 'Subject: Test 123 \n\n Today, I want to look into one of those cases of impatient and how the community has waited for that feature, to be specific, two upcoming functions.'
)