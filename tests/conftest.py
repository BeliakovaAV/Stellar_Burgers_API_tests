import pytest
import allure

from generators import generate_user_creation_body
from methods.user_creation_meth import UserCreationMethod
from methods.user_login_meth import UserLoginMethod


@pytest.fixture
def generate_user():
    user_body = generate_user_creation_body()
    access_token, response = UserCreationMethod.create_user_and_get_access_token(user_body)
    yield user_body, response
    UserCreationMethod.delete_user(access_token)


@pytest.fixture
def logged_in_user():
    body = generate_user_creation_body()
    UserCreationMethod.create_user(body)
    response = UserLoginMethod.user_login(body)
    long_token = response.json()["accessToken"]
    access_token = long_token.replace("Bearer ", "")
    yield body, access_token
    UserCreationMethod.delete_user(access_token)


@pytest.fixture  # ПОД ВОПРОСОМ
def cleanup_order():
    order_tracks = []

    def register_order_track(order_track):
        order_tracks.append(order_track)

    yield register_order_track

    for order_track in order_tracks:
        with allure.step('Удаляем созданное бронирование'):
            OrderCreationMethod.cancel_order(order_track)
