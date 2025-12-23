import pytest
import allure
from data_for_test.data_for_test import MyOrder

class TestOrderCreate:

    @allure.title("Проверка Создания заказа")
    @allure.step("Тест можно указать один из цветов, оба цвета, совсем не указывать цвет; тело ответа содержит track ")
    @pytest.mark.parametrize('color',(['BLACK'], ['GREY'], ['BLACK','GREY'], ['']))
    def test_order_choose_one_colour(self, order_api, color):
        payload = MyOrder.order
        payload["color"] = color
        response = order_api.create_order_rqst(payload)
        assert response.status_code  == 201
        assert 'track' in response.json()
    
