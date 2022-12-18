import pytest
import requests
from configuration import SERVICE_URL_NEW


@pytest.fixture()
def get_users():
    resp = requests.get(SERVICE_URL_NEW)
    return resp