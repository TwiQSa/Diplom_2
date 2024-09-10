import pytest
import data_for_tests
from helpers import *
import requests


@pytest.fixture(scope="function")
def create_and_login_user():
    user_data = generate_user_data()
    create_response = requests.post(data_for_tests.URL_USER_CREATION, json=user_data)

    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    login_response = requests.post(data_for_tests.URL_USER_LOGIN, json=login_data)

    yield {
        "accessToken":  login_response.json()["accessToken"],
        "user_data": user_data
    }

@pytest.fixture(scope="function")
def create_and_login_user_for_order_creation():
    user_data = generate_user_data_for_order_creation()
    create_response = requests.post(data_for_tests.URL_USER_CREATION, json=user_data)

    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    login_response = requests.post(data_for_tests.URL_USER_LOGIN, json=login_data)

    yield {
        "accessToken":  login_response.json()["accessToken"],
        "user_data": user_data
    }


