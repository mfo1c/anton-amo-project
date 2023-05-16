import requests


def get_answer(amo_messages):
    data = []
    print(amo_messages[0])
    return 'success'
    for amo_message in amo_messages:
        if amo_message:
            data.append({
                'text': amo_message['text'],
                'role': 'ai'
            })
    return 'OK'
    url = 'https://api.suvvy.ai/api/v1/predict/chat/placeholder'
    response = requests.post(url,
                             )
