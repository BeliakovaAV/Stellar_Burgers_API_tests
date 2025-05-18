import requests
from data import Url
from .user_creation_meth import UserCreationMethod  # под вопросом


class UserLoginMethod:

    @staticmethod
    def user_login(body):
        payload = {
            "email": body["email"],
            "password": body["password"]
        }
        return requests.post(f'{Url.BASE_URL}{Url.USER_LOGIN_URL}', json=payload)

    @staticmethod
    def change_login_body(email=None, password=None):
        payload = {}
        if email is not None:
            payload["email"] = email
        if password is not None:
            payload["password"] = password
        return requests.post(f'{Url.BASE_URL}{Url.USER_LOGIN_URL}', json=payload)

    @staticmethod
    def user_logout(refresh_token):
        body = {"token": "{{refreshToken}}"}
        return requests.post(f'{Url.BASE_URL}{Url.USER_LOGOUT_URL}', json=body)
