from twilio.rest import Client
#https://ntfy.sh/app better than twilio as per Andrei Neagoie

account_sid = '**********************************'
auth_token = '**********************************'
client = Client(account_sid, auth_token)

for i in range(5):
    message = client.messages.create(
    from_ = '+17626002616',
    body = f'hello hamza {i} time',
    to = '+962789115910'
    )

print(message.sid)


