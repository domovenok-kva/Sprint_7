import pytest
import allure
from data_for_test.data_for_test import ErrorNames

class TestCurierLogin:

    @allure.title("Проверка Логина курьера")
    @allure.step("Тест авторизация")
    def test_curier_auth(self, curier_api):
        payload = curier_api.generate_curier_data()
        response = curier_api.create_curier_rqst(payload)
        response = curier_api.login_curier_rqst(payload)
        assert response.status_code  == 200
        assert "id" in response.json()

    @allure.step("Тест система вернёт ошибку, если неправильно указать логин или пароль")
    @pytest.mark.parametrize('inpt', ["login", "password"])
    def test_curier_auth_invalid_inpt(self, curier_api, inpt):
        payload = curier_api.generate_curier_data()
        response = curier_api.create_curier_rqst(payload)
        payload[inpt] = 'invalid_data'
        response = curier_api.login_curier_rqst(payload)
        assert response.status_code  == 404
        assert response.json()['message'] == ErrorNames.accaunt_data_not_exist_err

    @allure.step("Тест если какого-то поля нет, запрос возвращает ошибку")
    @pytest.mark.parametrize('inpt', ["login", "password"])
    def test_curier_auth_empty_inpt(self, curier_api, inpt):
        payload = curier_api.generate_curier_data()
        response = curier_api.create_curier_rqst(payload)
        payload[inpt] = ''
        response = curier_api.login_curier_rqst(payload)
        assert response.status_code  == 400
        assert response.json()['message'] == ErrorNames.not_enough_data_for_login_err

    @allure.step("Тест если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_curier_auth_user_not_exist(self, curier_api):
        login = "User_who_donot_exist"
        password = "Pasword_not_exist"
        payload = curier_api.not_existed_curier_login(login, password)
        response = curier_api.login_curier_rqst(payload)
        assert response.status_code  == 404
        assert response.json()['message'] == ErrorNames.accaunt_data_not_exist_err


        