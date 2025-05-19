import allure
from methods.user_update_meth import UserUpdateMethod
from generators import generate_update_info
from data import ServerResponses


class TestUserUpdate:
    @allure.title('Тест на успешное обновление информации о пользователе с авторизацией')
    def test_successful_user_update(self, logged_in_user):
        with allure.step('Cоздаём пользователя и авторизуем его'):
            body, access_token = logged_in_user
        with allure.step('Готовим новую информацию о пользователе'):
            payload = generate_update_info()
        with allure.step('Обновляем информацию о пользователе'):
            response = UserUpdateMethod.user_update(payload, access_token)
            data = response.json()
        assert response.status_code == 200
        assert (
                data["success"] is True
                and data["user"] == {"email": payload["email"], "name": payload["name"]})

    @allure.title('Тест на безуспешное обновление информации о пользователе без авторизации')
    def test_failure_user_update(self, generate_user):
        with allure.step('Готовим новую информацию о пользователе'):
            payload = generate_update_info()
        with allure.step('Обновляем информацию о пользователе'):
            response = UserUpdateMethod.user_update(payload, access_token="")
            data = response.json()
        assert response.status_code == 401
        assert data == ServerResponses.USER_UPDATE_FAILURE
