import requests
from data import Url


class UserCreationMethod:
    @staticmethod
    def delete_user(access_token):
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER_URL}', headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        })

    @staticmethod
    def create_user_and_get_access_token(body):
        response = requests.post(f'{Url.BASE_URL}{Url.USER_CREATION_URL}', json=body)
        data = response.json()
        return data["accessToken"], response

    @staticmethod
    def create_user_and_get_refresh_token(body):
        response = requests.post(f'{Url.BASE_URL}{Url.USER_CREATION_URL}', json=body)
        data = response.json()
        return data["refreshToken"]

    @staticmethod
    def create_user(body):
        return requests.post(f'{Url.BASE_URL}{Url.USER_CREATION_URL}', json=body)
