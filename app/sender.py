import requests


def get_answer(amo_messages):
    data = []
    print(amo_messages[0], amo_messages[1])
    return 'success'
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
    print(data)
    url = 'https://api.suvvy.ai/api/v1/predict/chat/placeholder'
    response = requests.post(url, data=data)
    print('RESPONSE')
    print(response.text)
    return response.json()['prediction']
