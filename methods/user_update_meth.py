import requests
from data import Url


class UserUpdateMethod:
    @staticmethod
    def user_update(payload, access_token):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        return requests.patch(
            f"{Url.BASE_URL}{Url.USER_UPDATE_URL}", headers=headers, json=payload)
