import string
import allure
import requests
import json
from data_for_test.data_for_test import MyURLS

class OrderAPI:
   @allure.step("Создание заказа")
   def create_order_rqst(self, payload):
      return requests.post(MyURLS.create_order_url, data=json.dumps(payload))
   
   @allure.step("Получение заказа по его номеру")
   def get_order_by_number(self):
      return requests.get(MyURLS.order_list_url)
    