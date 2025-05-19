import pytest
import allure

from generators import generate_user_creation_body
from methods.user_creation_meth import UserCreationMethod
from methods.user_login_meth import UserLoginMethod
from methods.order_creation_meth import OrderCreationMethod


@pytest.fixture
def generate_user():
    user_body = generate_user_creation_body()
    access_token, response = UserCreationMethod.create_user_and_get_access_token(user_body)
    assert response.status_code == 200
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


@pytest.fixture
def generate_order():
    ingredients_ids = OrderCreationMethod.get_ingredient_ids()
    response = OrderCreationMethod.create_order(ingredients_ids)
    return response


