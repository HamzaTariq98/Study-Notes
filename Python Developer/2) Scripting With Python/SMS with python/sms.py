from twilio.rest import Client
#https://ntfy.sh/app better than twilio as per Andrei Neagoie

account_sid = 'ACa9c8adc6237c6fe9859b639a7f9d0eb2'
auth_token = '********************************'
client = Client(account_sid, auth_token)

for i in range(1):
    message = client.messages.create(
    from_ = '+17626002616',
    body = f'hello hamza {i} time',
    to = '+962789115910'
    )

print(message.sid)


