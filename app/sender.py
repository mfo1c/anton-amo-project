import requests


def get_answer(amo_messages):
    data = []
    for amo_message in amo_messages:
        if amo_message['author']['origin'] == 'amocrm':
            data.append({
                'text': amo_message['text'],
                'role': 'ai'
            })
        else:
            data.append({
                'text': amo_message['text'],
                'role': 'human'
            })
    print(len(data))
    url = 'https://api.suvvy.ai/api/v1/predict/chat/placeholder'
    response = requests.post(url, data=data)
    print('RESPONSE')
    print(response.text)
    return response.json()['prediction']
