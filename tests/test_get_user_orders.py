import pytest
import allure
import requests
import data_for_tests


class TestGetSpecificUserOrders:
    @allure.title('Получение заказов конкретного пользователя будучи авторизованным пользователем')
    @allure.description('Проверяем код статуса при получении заказов пользователя будучи авторизованным')
    def test_get_user_orders_with_auth(self, create_and_login_user_for_order_creation):
        headers = {"Authorization": create_and_login_user_for_order_creation['accessToken']}
        response = requests.get(data_for_tests.URL_GET_USER_ORDERS, headers=headers)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Получение заказов конкретного пользователя будучи неавторизованным пользователем')
    @allure.description('Проверяем код статуса и ошибку при получении заказов пользователя будучи неавторизованным')
    def test_get_user_orders_without_auth(self):
        response = requests.get(data_for_tests.URL_GET_USER_ORDERS)

        assert response.status_code == 401 and response.json()["message"] == data_for_tests.WITHOUT_AUTH
