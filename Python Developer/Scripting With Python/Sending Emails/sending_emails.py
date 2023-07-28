import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import os,sys

current_path = Path(sys.argv[0]).parent # Finding current path of script
os.chdir(current_path) # change cwd for desired path as in VScode cwd in desktop


def send_email(send_to ,email_subject,body_object):
    email = EmailMessage()
    email['to'] = send_to
    email['subject'] = email_subject
    email.set_content(body_object,subtype='html')

    with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('hamzatarq98@gmail.com', '*****************')
        smtp.send_message(email)
        print(f'sent for {send_to}')


send_to = ['hamzatarq98@gmail.com','hamzatarq98@gmail.com']
email_subject = 'this is an automated email'
body_object = Template(Path(current_path.joinpath('sample_email.html')).read_text()).substitute({'name':'hello'})

for email in send_to:
    send_email(send_to = email,email_subject = 'this is an automated email',body_object = body_object)
