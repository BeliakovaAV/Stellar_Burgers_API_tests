import requests
from data import Url


class UserUpdateMethod:

    @staticmethod
    def update_user(body, access_token):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        payload = {
            "email": body["email"],
            "name": body["name"]
        }
        return requests.patch(f'{Url.BASE_URL}{Url.USER_UPDATE_URL}', headers=headers, json=payload)

    @staticmethod
    def change_updating_body(email=None, name=None):
        payload = {}
        if email is not None:
            payload["email"] = email
        if name is not None:
            payload["name"] = name
        return requests.post(f'{Url.BASE_URL}{Url.USER_LOGIN_URL}', json=payload)
