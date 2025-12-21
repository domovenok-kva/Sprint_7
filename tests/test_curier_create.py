import pytest
import allure


class TestCurierCreation:

    @allure.title("Проверки на создание курьера")
    @allure.step("Тест создание курьера")
    def test_ctreate_new_curier(self, curier_api):
        payload  = curier_api.generate_curier_data()
        response = curier_api.create_curier_rqst(payload)
        assert response.status_code  == 201
        assert response.json() == {"ok": True}


    @allure.step("Тест нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_of_curier(self, curier_api):
        payload  = curier_api.generate_curier_data()
        response = curier_api.create_curier_rqst(payload)
        response = curier_api.create_curier_rqst(payload)
        assert response.status_code  == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'


    @allure.step("Тест если одного из полей нет, запрос возвращает ошибку")
    @pytest.mark.parametrize('inpt', ["login", "password"])
    def test_create_curier_one_inpt_empty(self, curier_api, inpt):
        payload = curier_api.generate_curier_data() 
        payload[inpt] = ''
        response = curier_api.create_curier_rqst(payload)
        assert response.status_code  == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.step("Тест если создать пользователя с логином, который уже есть, возвращается ошибка")
    def test_create_curier_with_exist_login(self, curier_api):
        curier_nmbr_one = curier_api.generate_curier_data()
        response = curier_api.create_curier_rqst(curier_nmbr_one)
        curier_nmbr_two = curier_api.generate_curier_data()
        curier_nmbr_two['login'] = curier_nmbr_one['login']
        response = curier_api.create_curier_rqst(curier_nmbr_two)
        assert response.status_code  == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'


