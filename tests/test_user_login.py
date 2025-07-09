import allure
from methods.user_login_meth import UserLoginMethod
from data import ServerResponses, TestData


class TestUserLogin:
    @allure.title('Тест на успешную авторизацию пользователя')
    def test_successful_user_login(self, generate_user):
        with allure.step('Cоздаём пользователя'):
            user_body, response = generate_user
        with allure.step('Авторизуем пользователя'):
            login = UserLoginMethod.user_login(user_body)
            data = login.json()
        assert login.status_code == 200
        assert (
                data["success"] is True
                and data["user"] == {"email": user_body["email"], "name": user_body["name"]}
                and data["accessToken"].startswith("Bearer ")
                and data["refreshToken"])

    @allure.title('Тест на ошибку при авторизации с неправильным полем Пароль')
    def test_wrong_password_failure(self, generate_user):
        with allure.step('Создаём пользователя'):
            user_body, response = generate_user
        with allure.step('Меняем тело авторизации(вставляем в поле Пароль неправильное значение)'):
            login = UserLoginMethod.change_login_body(email=user_body["email"],
                                                      password=TestData.WRONG_PASSWORD)
        assert login.status_code == 401 and login.json() == ServerResponses.USER_LOGIN_FAILURE

    @allure.title('Тест на ошибку при авторизации с неправильным полем Email')
    def test_wrong_email_failure(self, generate_user):
        with allure.step('Создаём пользователя'):
            user_body, response = generate_user
        with allure.step('Меняем тело авторизации(вставляем в поле Email неправильное значение)'):
            login = UserLoginMethod.change_login_body(email=TestData.WRONG_EMAIL,
                                                      password=user_body["password"])
        assert login.status_code == 401 and login.json() == ServerResponses.USER_LOGIN_FAILURE
