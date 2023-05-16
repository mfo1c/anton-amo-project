import requests
from app import auth
import json



def send_message(receiver_id: str, message: str):
    print(message, 'answer')
    account_chat_id, x_auth = auth.get_tokens()

    headers = {'X-Auth-Token': x_auth}
    url = f'https://amojo.amocrm.ru/v1/chats/{account_chat_id}/' \
          f'{receiver_id}/messages?with_video=true&stand=v15'
    requests.post(url, headers=headers, data=json.dumps({"text": message}))


def get_chat_history(receiver_id: str):
    account_chat_id, x_auth = auth.get_tokens()

    headers = {'X-Auth-Token': x_auth}
    url = f'https://amojo.amocrm.ru/messages/{account_chat_id}/merge?stand=v15' \
          f'&offset=0&limit=100&chat_id%5B%5D={receiver_id}&get_tags=true&lang=ru'
    message_list = requests.get(url, headers=headers).json()
    return message_list['message_list']