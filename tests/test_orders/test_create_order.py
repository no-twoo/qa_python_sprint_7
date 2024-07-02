import json
import pytest
import allure
from http import HTTPStatus
from helpers import *


class TestOrderCreation:
    @allure.title('Проверка успешного создания заказа')
    @allure.description('Тест проверяет, что заказ можно создать с указанием предложенных цветов, с одним из цветов, '
                        'и без цветов, возвращается код 201 и тело ответа содержит трек')
    @pytest.mark.parametrize(
        'first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color',
        [
            ("Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2020-06-06",
             "Saske, come back to Konoha", ["BLACK"]
             ),
            ("Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2020-06-06",
             "Saske, come back to Konoha", ["GREY"]
             ),
            ("Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2020-06-06",
             "Saske, come back to Konoha", ["BLACK", "GREY"]
             ),
            ("Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2020-06-06",
             "Saske, come back to Konoha", []
             ),
        ]
    )
    def test_create_order(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date,
                          comment, color):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }

        json_body = json.dumps(payload)

        response = Requests.requests_post_create_order(json_body)

        assert response.status_code == HTTPStatus.CREATED and response.json()["track"]
