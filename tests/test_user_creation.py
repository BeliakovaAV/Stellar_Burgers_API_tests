import allure
from methods.user_creation_meth import UserCreationMethod
import helpers
from data import ServerResponses


class TestCreateUser:
    @allure.title('Тест на успешное создание пользователя')
    def test_successful_user_creation(self, generate_user):
        with allure.step('Создаём пользователя'):
            user_body, response = generate_user
            data = response.json()
        assert response.status_code == 200
        assert (
                data["success"] is True
                and data["user"] == {"email": user_body["email"], "name": user_body["name"]}
                and data["accessToken"].startswith("Bearer ")
                and data["refreshToken"]
        )

    @allure.title('Тест на невозможность создания двух одинаковых пользователей')
    def test_double_user_creation_impossible(self, generate_user):
        with allure.step('Создаём первого пользователя'):
            user_body, response = generate_user
        with allure.step('Создаём второго курьера - копию первого'):
            doppelganger = UserCreationMethod.create_user(user_body)
        assert doppelganger.status_code == 403 and doppelganger.json() == ServerResponses.SAME_USER_CREATION_FAILURE

    @allure.title('Тест на ошибку при пустом обязательном поле Email')
    def test_empty_email_field_error(self):
        with allure.step('Создаём пользователя без email'):
            user_body = helpers.modify_create_user_body("email", "")
            user = UserCreationMethod.create_user(user_body)
        assert user.status_code == 403 and user.json() == ServerResponses.EMPTY_FIELD_CREATION_FAILURE

    @allure.title('Тест на ошибку при пустом обязательном поле Пароль')
    def test_empty_password_field_error(self):
        with allure.step('Создаём пользователя без пароля'):
            user_body = helpers.modify_create_user_body("password", "")
            user = UserCreationMethod.create_user(user_body)
        assert user.status_code == 403 and user.json() == ServerResponses.EMPTY_FIELD_CREATION_FAILURE

    @allure.title('Тест на ошибку при пустом обязательном поле Имя')
    def test_empty_name_field_error(self):
        with allure.step('Создаём пользователя без имени'):
            user_body = helpers.modify_create_user_body("name", "")
            user = UserCreationMethod.create_user(user_body)
        assert user.status_code == 403 and user.json() == ServerResponses.EMPTY_FIELD_CREATION_FAILURE
