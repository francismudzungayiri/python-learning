from twilio.rest import Client 


#account_ssid = ''
#account_auth = ''

client = Client(account_ssid, account_auth)

#twilio_number = ''
#my_number = ''

message = client.messages.create(
    body="Hello from Francis I am learning how to send sms using python code",
    from_= twilio_number,
    to= my_number
)

print(message.sid)
