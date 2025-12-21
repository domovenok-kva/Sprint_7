import pytest
import allure
from data_for_test.data_for_test import MyOrder

class TestOrderCreate:

    @allure.title("Проверка Создания заказа")
    @allure.step("Тест можно указать один из цветов — BLACK или GREY")
    @pytest.mark.parametrize('color',(['BLACK'], ['GREY']))
    def test_order_choose_one_colour(self, order_api, color):
        payload = MyOrder.order
        payload["color"] = color
        response = order_api.create_order_rqst(payload)
        assert response.status_code  == 201

    @allure.step("Тест можно указать оба цвета")
    @pytest.mark.parametrize('color',(['BLACK','GREY']))
    def test_order_choose_two_colours(self, order_api, color):
        payload = MyOrder.order
        payload["color"] = color
        response = order_api.create_order_rqst(payload)
        assert response.status_code  == 201

    @allure.step("Тест можно совсем не указывать цвет")
    @pytest.mark.parametrize('color', [''])
    def test_order_choose_none_colour(self, order_api, color):
        payload = MyOrder.order
        payload["color"] = color
        response = order_api.create_order_rqst(payload)
        assert response.status_code  == 201

    @allure.step("Тест тело ответа содержит track")
    def test_order_response_have_track(self, order_api):
        payload = MyOrder.order
        response = order_api.create_order_rqst(payload)
        assert response.status_code  == 201
        assert 'track' in response.json()

    
