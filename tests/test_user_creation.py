import pytest
import requests
import allure
import data_for_tests
from helpers import *

class TestUserCreation:

    @allure.title('Создание уникального пользователя')
    @allure.description('Проверяем код статуса при создании уникального пользователя со всеми заполненными данными')
    def test_unique_user_creation(self):
        data = generate_user_data()
        response = requests.post(data_for_tests.URL_USER_CREATION, json=data)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    @allure.description('Проверяем код статуса и текст ошибки при создании пользователя, который уже зарегистрирован')
    def test_existing_user_creation(self):
        user_data = generate_user_data()
        response = requests.post(data_for_tests.URL_USER_CREATION, json=user_data)
        response = requests.post(data_for_tests.URL_USER_CREATION, json=user_data)

        assert response.status_code == 403 and response.json()["message"] == data_for_tests.USER_ALREADY_EXISTS

    @allure.title('Создание пользователя без заполнения одного из обязательных полей')
    @allure.description('Проверяем код и текст ошибки при создании пользователя без заполнения обязательных полей')
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_with_missing_field(self, missing_field):
        data = generate_user_data()
        del data[missing_field]
        response = requests.post(data_for_tests.URL_USER_CREATION, json=data)

        assert (response.status_code == 403 and response.json()["message"] ==
                data_for_tests.INCOMPLETE_DATA_FOR_REGISTRATION)