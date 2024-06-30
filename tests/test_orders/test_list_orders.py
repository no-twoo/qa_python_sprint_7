import allure
from http import HTTPStatus
from helpers import *


class TestListOrders:
    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    @allure.description('Тест проверяет, что в тело ответа возвращается список заказов, возвращается код 200')
    def test_list_orders(self):
        response = Requests.requests_get_list_orders()

        assert response.status_code == HTTPStatus.OK and response.json()['orders']
