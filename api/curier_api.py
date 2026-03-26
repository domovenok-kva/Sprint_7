import random
import string
import allure
import requests
from data_for_test.data_for_test import MyURLS

class CurierAPI:
   
   @allure.step("Запрос на создание курьера")
   def create_curier_rqst(self, payload):
      return requests.post(MyURLS.create_curier_url, data=payload)
    
   @allure.step("Запрос на залогин")
   def login_curier_rqst(self, payload):
      return requests.post(MyURLS.login_curier_url, data=payload)

   @allure.step("Генерация рандомных данных для формы")
   def generate_random_string(length):
      letters = string.ascii_lowercase
      random_string = ''.join(random.choice(letters) for i in range(length))
      return random_string
     
   @allure.step("Создаём курьера")
   def generate_curier_data(self):
      login = CurierAPI.generate_random_string(10)
      password = CurierAPI.generate_random_string(10)
      first_name = CurierAPI.generate_random_string(10)

      return {
         "login": login,
         "password": password,
         "firstName": first_name
         }
   
   @allure.step("Вход уже зарегестрированного пользователя")
   def not_existed_curier_login(self, login, password):
      payload = {
       "login": login,
       "password": password,
       }
      return payload
     

