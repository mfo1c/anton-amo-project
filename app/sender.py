import requests


def get_answer(chat_history):
    print(chat_history)
    return 'OK'
    url = 'https://api.suvvy.ai/api/v1/predict/chat/placeholder'
    response = requests.post(url,
                             data={
                                 
                             })
