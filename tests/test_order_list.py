import allure
from data_for_test.data_for_test import MyOrder

class TestOrderList:
    @allure.title("Проверка  Список заказов")
    @allure.step("Тест в тело ответа возвращается список заказов.")
    def test_order_list_return_to_body(self, order_api):
        response = order_api.get_order_by_number()
        assert response.status_code == 200
        assert "orders" in response.json()