from helpers import *
from data import *
import allure
from http import HTTPStatus


class TestCourierLogin:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Тест проверяет, что курьер может авторизоваться, возвращается код 200')
    def test_login_courier_successful(self):
        payload_create_courier = create_registration_payload()

        payload_login_courier = {
            "login": payload_create_courier["login"],
            "password": payload_create_courier["password"]
        }
        Requests.requests_post_create(payload_create_courier)

        response_login_courier = Requests.requests_post_login(payload_login_courier)

        assert response_login_courier.status_code == HTTPStatus.OK and response_login_courier.json()["id"]

    @allure.title('Проверка авторизации курьера без логина')
    @allure.description('Тест проверяет, что курьер не может авторизоваться без логина, возвращается код 400 и '
                        'ошибка в теле ответа')
    def test_login_courier_without_login(self):
        payload_create_courier = create_registration_payload()
        payload_login_courier = {
            "login": '',
            "password": payload_create_courier["password"]
        }
        Requests.requests_post_create(payload_create_courier)

        response_without_login_courier = Requests.requests_post_login(payload_login_courier)

        assert (response_without_login_courier.status_code == HTTPStatus.BAD_REQUEST and
                response_without_login_courier.json()['message'] == MESSAGE_3)

    @allure.title('Проверка авторизации курьера без пароля')
    @allure.description('Тест проверяет, что курьер не может авторизоваться без пароля, возвращается код 400 и '
                        'ошибка в теле ответа')
    def test_login_courier_without_password(self):
        payload_create_courier = create_registration_payload()
        payload_login_courier = {
            "login": payload_create_courier["login"],
            "password": ''
        }
        Requests.requests_post_create(payload_create_courier)

        response_without_login_courier = Requests.requests_post_login(payload_login_courier)

        assert (response_without_login_courier.status_code == HTTPStatus.BAD_REQUEST and
                response_without_login_courier.json()['message'] == MESSAGE_3)

    @allure.title('Проверка авторизации курьера с неправильным или несуществующим логином')
    @allure.description('Тест проверяет, что курьер не может авторизоваться с неправильным или несуществующим '
                        'логином, возвращается код 404 и ошибка в теле ответа')
    def test_login_courier_with_incorrect_login(self):
        payload_create_courier = create_registration_payload()
        payload_login_courier = {
            "login": 'incorrect_login',
            "password": payload_create_courier["password"]
        }
        Requests.requests_post_create(payload_create_courier)

        response_without_login_courier = Requests.requests_post_login(payload_login_courier)

        assert (response_without_login_courier.status_code == HTTPStatus.NOT_FOUND and
                response_without_login_courier.json()['message'] == MESSAGE_4)

    @allure.title('Проверка авторизации курьера с неправильным паролем')
    @allure.description('Тест проверяет, что курьер не может авторизоваться с неправильным паролем, возвращается '
                        'код 404 и ошибка в теле ответа')
    def test_login_courier_with_incorrect_password(self):
        payload_create_courier = create_registration_payload()
        payload_login_courier = {
            "login": payload_create_courier["login"],
            "password": '123456'
        }
        Requests.requests_post_create(payload_create_courier)

        response_without_login_courier = Requests.requests_post_login(payload_login_courier)

        assert (response_without_login_courier.status_code == HTTPStatus.NOT_FOUND and
                response_without_login_courier.json()['message'] == MESSAGE_4)
