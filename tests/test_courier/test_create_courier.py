import pytest
import requests
from helpers import *
from data import *
import allure


class TestCourierCreation:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Тест проверяет, что при успешном создании курьера возвращается код 201 и значение в теле '
                        'ответа True')
    def test_create_courier_successful(self):
        response = requests.post(f'{test_url}/api/v1/courier', data=register_new_courier_and_return_login_password())

        assert response.status_code == 201 and response.json()["ok"]

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    @allure.description('Тест проверяет, что при создании курьеров с одинаковыми данными возвращается код 409 и '
                        'ошибка в теле ответа')
    def test_create_two_identical_couriers(self):
        payload = register_new_courier_and_return_login_password()
        requests.post(f'{test_url}/api/v1/courier', data=payload)

        repeat_response = requests.post(f'{test_url}/api/v1/courier', data=payload)

        assert repeat_response.status_code == 409 and repeat_response.json()["message"] == message_1

    @allure.title('Проверка создания курьера без логина или пароля')
    @allure.description('Тест проверяет, что при создании курьеров без логина или пароля возвращается код 400 и '
                        'ошибка в теле ответа')
    @pytest.mark.parametrize(
        'login, password, first_name',
        [
            ('', generate_random_string(10), generate_random_string(10)),
            (generate_random_string(10), '', generate_random_string(10)),
        ]
    )
    def test_create_courier_without_login_or_password(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{test_url}/api/v1/courier', data=payload)

        assert response.status_code == 400 and response.json()["message"] == message_2

    @allure.title('Проверка создания курьера с обязательными полями')
    @allure.description('Тест проверяет, что курьера можно создать заполнив обязательные поля, возвращается код 201')
    def test_create_courier_with_required_fields(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f'{test_url}/api/v1/courier', data=payload)

        assert response.status_code == 201 and response.json()["ok"]
