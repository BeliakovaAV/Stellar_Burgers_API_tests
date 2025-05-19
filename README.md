## Дипломный проект. Задание 2: API-тесты
<hr>

## Студент: Алевтина Белякова

## <h>Когорта: #18</h>
<hr>

## <h>Project: Stellar Burger API</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла         | Содержание файла                        |
|------------------------|-----------------------------------------|
| Tests dir              | Директория с тестами                    |
| test_order_creation.py | Тесты на создание заказа                |
| test_user_creation.py  | Тесты на удаление бронирования          |
| test_user_login.py     | Тесты на авторизацию пользователя       |
| test_user_orders.py    | Тесты на получение заказов пользователя |
| test_user_update.py    | Тесты на обновление данных пользователя |
| conftest.py            | Фикстуры                                |
| helpers.py             | Хэлперы для тела запросов               |
| data.py                | Файл с URL и body запросов              |
| Methods dir            | Директория с методами                   |
| order_creation_meth.py | Методы создания заказа                  |
| user_creation_meth.py  | Методы создания пользователя            |
| user_login_meth.py     | Методы авторизации пользователя         |
| user_orders_meth.py    | Методы получения заказов пользователя   |
| user_update_meth.py    | Методы обновления данных пользователя   |
| generators.py          | Генератор данных                        |
| requirements.txt       | Файл с зависимостями                    |
| allure_results.dir     | Папка с отчетами Allure                 |


