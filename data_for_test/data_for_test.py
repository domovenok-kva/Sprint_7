class MyURLS:
    test_service_url = 'http://qa-scooter.praktikum-services.ru/'
    create_curier_url = f'{test_service_url}api/v1/courier'
    login_curier_url = f'{test_service_url}api/v1/courier/login'
    create_order_url = f'{test_service_url}api/v1/orders'
    order_list_url = f'{test_service_url}api/v1/orders'

class MyOrder:
    order = {
        "firstName": "Ion",
        "lastName": "Tikhyy",
        "address": "Pushkin st 5",
        "metroStation": 4,
        "phone": "8 800 555 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-12-25",
        "comment": "Самокат требуют наши сердца",
        "color": [
            "BLACK"
         ]
    }

