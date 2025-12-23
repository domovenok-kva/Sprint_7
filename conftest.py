import pytest
from api.curier_api import CurierAPI
from api.order_api import OrderAPI

@pytest.fixture()
def curier_api():
    cur_api = CurierAPI()
    yield cur_api

@pytest.fixture()
def order_api():
    yield OrderAPI()