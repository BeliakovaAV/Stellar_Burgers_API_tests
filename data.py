class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    USER_CREATION_URL = '/api/auth/register'
    USER_LOGIN_URL = '/api/auth/login'
    USER_LOGOUT_URL = '/api/auth/logout' #ВОПРОС
    TOKEN_UPDATE_URL = '/api/auth/token' #ВОПРОС
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
    ORDER_CREATION_SUCCESS = {"name": "Краторный метеоритный бургер",  # ПРИМЕР
                              "order": {"number": 6257},
                              "success": True}
    ORDER_CREATION_FAILURE = {"success": False,
                              "message": "Ingredient ids must be provided"}
    USER_ORDERS_LIST_SUCCESS = {"success": True,
                                "orders": [
                                    {"ingredients": ["60d3463f7034a000269f45e9", "60d3463f7034a000269f45e7"], "_id": "",
                                     "status": "done", "number": 1, "createdAt": "2021-06-23T20:11:01.403Z",
                                     "updatedAt": "2021-06-23T20:11:01.406Z"},
                                    {"ingredients": ["60d3463f7034a000269f45e9"], "_id": "", "status": "done",
                                     "number": 3, "createdAt": "2021-06-23T20:13:23.654Z",
                                     "updatedAt": "2021-06-23T20:13:23.657Z"}], "total": 2, "totalToday": 2}
    USER_ORDERS_LIST_FAILURE = {"success": False,
                                "message": "You should be authorised"}


class TestData:
    WRONG_EMAIL = "testdata10@yandex.ru"
    WRONG_PASSWORD = "1234567"
    UPDATED_EMAIL = "testdata20@yandex.ru"
    UPDATED_NAME = "clara"
    WRONG_INGREDIENT_HASH = "6037fhdsbj38dbd67fb63bf"
