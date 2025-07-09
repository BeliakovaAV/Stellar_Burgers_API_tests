import allure
from methods.user_orders_meth import OrderListMethod
from data import ServerResponses, TestData
import helpers


class TestUserOrdersList:
    @allure.title('Тест на успешное получение списка заказов конкретного пользователя с авторизацией')
    def test_successful_user_orders_with_auth(self, logged_in_user):
        with allure.step('Авторизуем пользователя и получаем access_token'):
            _, access_token = logged_in_user
        with allure.step('Получаем список заказов пользователя с аутентификацией'):
            response = OrderListMethod.get_user_orders(access_token)
            data = response.json()
        assert response.status_code == 200
        assert data["success"]
        assert helpers.validate_user_orders_structure(data["orders"], TestData.REQUIRED_USER_ORDER_FIELDS)

    @allure.title('Тест на безуспешное получение списка заказов конкретного пользователя без авторизации')
    def test_user_orders_no_auth_failure(self):
        with allure.step('Получаем список заказов пользователя с аутентификацией'):
            response = OrderListMethod.get_user_orders("")
            data = response.json()
        assert response.status_code == 401
        assert data == ServerResponses.USER_ORDERS_LIST_FAILURE

