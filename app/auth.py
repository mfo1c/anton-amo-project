import time

import requests

import secret_info


def get_token():
    try:
        session = requests.Session()
        print(secret_info.env_info)
        response = session.get(secret_info.env_info.account_url + "/")
        session_id = response.cookies.get('session_id')
        csrf_token = response.cookies.get('csrf_token')
        headers = {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': f'session_id={session_id}; '
                      f'csrf_token={csrf_token};'
                      f'last_login={secret_info.env_info.login}',
            'Host': f'{secret_info.env_info.account_url}'.replace('https://'),
            'Origin': f'{secret_info.env_info.account_url}',
            'Referer': f'{secret_info.env_info.account_url}/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        payload = {
            'csrf_token': csrf_token,
            'password': secret_info.env_info.password,
            'temporary_auth': "N",
            'username': secret_info.env_info.login}
        print(headers)
        print(payload)
        response = session.post(f'{secret_info.env_info.account_url}/oauth2/authorize', headers=headers, data=payload)
        access_token = response.cookies.get('access_token')
        refresh_token = response.cookies.get('refresh_token')
        headers['access_token'] = access_token
        headers['refresh_token'] = refresh_token
        print(headers)
        payload = {
            'request[chats][session][action]': 'create'
        }
        response = session.post(f'{secret_info.env_info.account_url}/ajax/v1/chats/session', headers=headers, data=payload)
        token = response.json()['response']['chats']['session']['access_token']
    except Exception as e:
        print(e)
        time.sleep(3)
        return get_token()
    print('New token:', token)
    return token

