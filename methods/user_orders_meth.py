import requests
from data import Url


class OrderListMethod:
    @staticmethod
    def get_user_orders(access_token):
        return requests.get(f'{Url.BASE_URL}{Url.USER_ORDERS_LIST_URL}', headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        })
