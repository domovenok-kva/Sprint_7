import pytest
from api.curier_api import CurierAPI
from api.order_api import OrderAPI


@pytest.fixture()
def curier_api():
    return CurierAPI()

@pytest.fixture()
def order_api():
    return OrderAPI()