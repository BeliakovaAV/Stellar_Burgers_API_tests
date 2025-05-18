import requests
from data import Url


class OrderCreationMeth:
    @staticmethod
    def create_order(ingredients_ids):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_CREATION_URL}', json={"ingredients": ingredients_ids})

    @staticmethod
    def get_ingredient_ids():
        response = requests.get(f'{Url.BASE_URL}{Url.INGREDIENTS_INFO_URL}')
        data = response.json()
        return [item["_id"] for item in data["data"]]

