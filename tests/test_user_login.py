import pytest
import requests
import allure
import data_for_tests

class TestUserLogin:

    @allure.title('Логин под существующим пользователем')
    @allure.description('Проверяем код статуса при входе под существующим пользователем')
    def test_login_existing_user(self, create_and_login_user):
        data = {
            "email": create_and_login_user["user_data"]["email"],
            "password": create_and_login_user["user_data"]["password"]
        }

        response = requests.post(data_for_tests.URL_USER_LOGIN, json=data)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Вход с неверным логином и паролем')
    @allure.description('Проверяем код статуса и ошибку при входе с неверным логином и паролем')
    @pytest.mark.parametrize("wrong_login_data", [
        {"email": "nesychestvyishuiiemail@gmail.com", "password": "wrongpassword"},
        {"email": "wronglogintest555@gmail.com", "password": "wrongpassword123"}
    ])
    def test_login_incorrect_data(self, wrong_login_data):
        response = requests.post(data_for_tests.URL_USER_LOGIN, json=wrong_login_data)
        assert response.status_code == 401 and response.json()["message"] == data_for_tests.INCORRECT_DATA_FOR_LOGIN

