from twilio.rest import Client
import os
from dotenv import load_dotenv


def send_msg():
    try:
        load_dotenv()
        account_sid = os.getenv('account_sid')
        auth_token = os.getenv('auth_token')
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='Hi, Mirshod',
            from_=os.getenv('from_'),
            to='+821067881928')

        print(message.sid)
        print("Message was sent successfully!")
    except:
        print("An error occurred!")


send_msg()