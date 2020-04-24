import time
import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')

version_api = '5.103'
url_vk = 'https://api.vk.com/method/users.get'


def get_status(user_id):
    data = {
        'user_ids': user_id,
        'v': version_api,
        'access_token': os.getenv('token_vk'),
        'fields': 'online',
    }
    response = requests.post(url_vk, params=data)
    online_or_not = response.json()['response'][0]['online']
    return online_or_not


def sms_sender(sms_text):

    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body=f"{sms_text}",
            from_=NUMBER_FROM,
            to=NUMBER_TO
        )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
