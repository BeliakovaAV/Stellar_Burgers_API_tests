class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    USER_CREATION_URL = '/api/auth/register'
    USER_LOGIN_URL = '/api/auth/login'
    USER_UPDATE_URL = '/api/auth/user'
    DELETE_USER_URL = '/api/auth/user'
    ORDER_CREATION_URL = '/api/orders'
    INGREDIENTS_INFO_URL = '/api/ingredients'
    USER_ORDERS_LIST_URL = '/api/orders'


class DataForUserCreation:
    CREATE_USER_BODY = {
        "email": "creatif@yandex.ru",
        "password": "1234",
        "name": "Donald"
    }


class ServerResponses:
    SAME_USER_CREATION_FAILURE = {"success": False,
                                  "message": "User already exists"}
    EMPTY_FIELD_CREATION_FAILURE = {"success": False,
                                    "message": "Email, password and name are required fields"}
    USER_LOGIN_FAILURE = {"success": False,
                          "message": "email or password are incorrect"}
    USER_UPDATE_FAILURE = {"success": False,
                           "message": "You should be authorised"}
    ORDER_CREATION_FAILURE = {"success": False,
                              "message": "Ingredient ids must be provided"}
    USER_ORDERS_LIST_FAILURE = {"success": False,
                                "message": "You should be authorised"}


class TestData:
    WRONG_EMAIL = "testdata10@yandex.ru"
    WRONG_PASSWORD = "1234567"
    WRONG_INGREDIENT_HASH = "6037fhdsbj38dbd67fb63bf"
