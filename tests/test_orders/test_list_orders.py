import requests
from data import *
import allure


class TestListOrders:
    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    @allure.description('Тест проверяет, что в тело ответа возвращается список заказов, возвращается код 200')
    def test_list_orders(self):
        response = requests.get(f'{test_url}/api/v1/orders')

        assert response.status_code == 200 and response.json()['orders']
