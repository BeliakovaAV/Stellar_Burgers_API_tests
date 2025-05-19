import allure
from methods.order_creation_meth import OrderCreationMethod
import helpers
from data import ServerResponses, TestData


class TestOrderCreation:
    @allure.title('Тест на успешное создание заказа авторизованным пользователем и ингредиентами')
    def test_create_order_with_auth(self, logged_in_user, generate_order):
        with allure.step('Создаем заказ с ингредиентами'):
            order = generate_order
            data = order.json()
        assert order.status_code == 200
        assert data == {
            "success": True,
            "order": {"number": data["order"]["number"]},
            "name": data["name"],
        }

    @allure.title('Тест на безуспешное создание заказа неавторизованным пользователем')  # ВОПРОС
    def test_create_order_no_auth_failure(self, generate_order):
        with allure.step('Создаем заказ с иннридиентами'):
            order = generate_order
            data = order.json()
        assert order.status_code == 401

    @allure.title('Тест на безуспешное создание заказа авторизованным пользователем без ингредиентов')
    def test_create_order_with_auth_no_ingredients(self, logged_in_user):
        with allure.step('Создаем заказ без ингредиентов'):
            order = OrderCreationMethod.create_order("")
            data = order.json()
        assert order.status_code == 400
        assert data == ServerResponses.ORDER_CREATION_FAILURE

    @allure.title('Тест на безуспешное создание заказа авторизованным пользователем c неправильным хэшем ингредиента')
    def test_create_order_with_auth_wrong_hash_ingredients(self, logged_in_user):
        with allure.step('Создаем заказ с неправильным хэшем ингредиента'):
            order = OrderCreationMethod.create_order(TestData.WRONG_INGREDIENT_HASH)
        assert order.status_code == 500
