from helpers import *
import requests
from data import *
import allure


class TestCourierLogin:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Тест проверяет, что курьер может авторизоваться, возвращается код 200')
    def test_login_courier_successful(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload_create_courier = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        payload_login_courier = {
            "login": login,
            "password": password
        }
        requests.post(f'{test_url}/api/v1/courier', data=payload_create_courier)

        response_login_courier = requests.post(f'{test_url}/api/v1/courier/login', data=payload_login_courier)

        assert response_login_courier.status_code == 200 and response_login_courier.json()["id"]

    @allure.title('Проверка авторизации курьера без логина')
    @allure.description('Тест проверяет, что курьер не может авторизоваться без логина, возвращается код 400 и '
                        'ошибка в теле ответа')
    def test_login_courier_without_login(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        payload_create_courier = {
            "login": login,
            "password": password,
        }
        payload_login_courier = {
            "login": '',
            "password": password
        }
        requests.post(f'{test_url}/api/v1/courier', data=payload_create_courier)

        response_without_login_courier = requests.post(f'{test_url}/api/v1/courier/login', data=payload_login_courier)

        assert (response_without_login_courier.status_code == 400 and response_without_login_courier.json()['message']
                == message_3)

    @allure.title('Проверка авторизации курьера без пароля')
    @allure.description('Тест проверяет, что курьер не может авторизоваться без пароля, возвращается код 400 и '
                        'ошибка в теле ответа')
    def test_login_courier_without_password(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        payload_create_courier = {
            "login": login,
            "password": password
        }
        payload_login_courier = {
            "login": login,
            "password": ''
        }
        requests.post(f'{test_url}/api/v1/courier', data=payload_create_courier)

        response_without_login_courier = requests.post(f'{test_url}/api/v1/courier/login', data=payload_login_courier)

        assert (response_without_login_courier.status_code == 400 and response_without_login_courier.json()['message']
                == message_3)

    @allure.title('Проверка авторизации курьера с неправильным или несуществующим логином')
    @allure.description('Тест проверяет, что курьер не может авторизоваться с неправильным или несуществующим '
                        'логином, возвращается код 404 и ошибка в теле ответа')
    def test_login_courier_with_incorrect_login(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        payload_create_courier = {
            "login": login,
            "password": password
        }
        payload_login_courier = {
            "login": 'incorrect_login',
            "password": password
        }
        requests.post(f'{test_url}/api/v1/courier', data=payload_create_courier)

        response_without_login_courier = requests.post(f'{test_url}/api/v1/courier/login', data=payload_login_courier)

        assert (response_without_login_courier.status_code == 404 and response_without_login_courier.json()['message']
                == message_4)

    @allure.title('Проверка авторизации курьера с неправильным паролем')
    @allure.description('Тест проверяет, что курьер не может авторизоваться с неправильным паролем, возвращается '
                        'код 404 и ошибка в теле ответа')
    def test_login_courier_with_incorrect_password(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        payload_create_courier = {
            "login": login,
            "password": password
        }
        payload_login_courier = {
            "login": login,
            "password": '123456'
        }
        requests.post(f'{test_url}/api/v1/courier', data=payload_create_courier)

        response_without_login_courier = requests.post(f'{test_url}/api/v1/courier/login', data=payload_login_courier)

        assert (response_without_login_courier.status_code == 404 and response_without_login_courier.json()['message']
                == message_4)
