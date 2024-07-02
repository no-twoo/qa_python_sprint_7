import random
import string
import requests
from data import *


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


# метод генерирует логин, пароль и имя курьера и возвращает список
def create_registration_payload():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


class Requests:
    # метод формирует post запрос на создание курьера
    @staticmethod
    def requests_post_create(data):
        return requests.post(f'{TEST_URL}/api/v1/courier', data=data)

    # метод формирует post запрос на авторизацию курьера
    @staticmethod
    def requests_post_login(data):
        return requests.post(f'{TEST_URL}/api/v1/courier/login', data=data)

    # метод формирует get запрос на возвращение списка заказов
    @staticmethod
    def requests_get_list_orders():
        return requests.get(f'{TEST_URL}/api/v1/orders')

    # метод формирует post запрос на проверку успешного заказа
    @staticmethod
    def requests_post_create_order(data):
        return requests.post(f'{TEST_URL}/api/v1/orders', data=data)
