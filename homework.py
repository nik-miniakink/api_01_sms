import time
import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()


def get_status(user_id):
    data = {
        'user_ids': user_id,
        'v': '5.103',
        'access_token': os.getenv('token_vk')
        'fields':'online',

    }
    friends_list = requests.post('https://api.vk.com/method/users.get', params=data)
    return friends_list


def sms_sender(sms_text):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    NUMBER_FROM = os.getenv('NUMBER_FROM')
    NUMBER_TO = os.getenv('NUMBER_TO')
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
