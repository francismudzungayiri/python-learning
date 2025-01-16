#Email Slicer
#Input an email address and extract the username and domain.


email = 'fmudzungayiri@gmail.com'


splitted_email = email.split('@')
username = splitted_email[1]
domain_name = splitted_email[1]

print(f'Username : {username}')
print(f'Domain name: {domain_name}')


