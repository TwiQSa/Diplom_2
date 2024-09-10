import pytest
import requests
import allure
import data_for_tests
from helpers import *


class TestUserDataUpdate:

    @allure.title('Изменение данных пользователя с авторизацией')
    @allure.description('Проверяем код статуса и новые данные, после изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize("new_data", [generate_user_data2(), generate_user_data2()])
    def test_update_user_data_with_auth(self, create_and_login_user, new_data):
        headers = {"Authorization": create_and_login_user['accessToken']}
        response = requests.patch(data_for_tests.URL_USER_DATA_UPDATE,
                                  json={"email": new_data["email"], "name": new_data["name"],
                                        "password": new_data["password"]}, headers=headers)

        assert (
                response.status_code == 200 and
                response.json()["success"] is True and
                response.json()["user"]["email"] == new_data["email"] and
                response.json()["user"]["name"] == new_data["name"]
        )

    @allure.title('Изменение данных пользователя без авторизации')
    @allure.description('Проверяем код статуса и ошибку, после изменение данных пользователя без авторизации')
    @pytest.mark.parametrize("new_data", data_for_tests.test_user_data_update_without_auth)
    def test_update_user_data_without_auth(self, new_data):
        response = requests.patch(data_for_tests.URL_USER_DATA_UPDATE, json=new_data)

        assert response.status_code == 401 and response.json()["message"] == data_for_tests.WITHOUT_AUTH
