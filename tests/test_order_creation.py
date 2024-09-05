import pytest
import requests
import allure
import data_for_tests


class TestOrderCreation:

    @allure.title('Создание заказа с авторизацией')
    @allure.description('Проверяем код статуса при создании с авторизацией и создания с ингредиентами')
    def test_create_order_with_auth(self, create_and_login_user_for_order_creation):
        headers = {"Authorization": create_and_login_user_for_order_creation['accessToken']}

        response = requests.post(data_for_tests.URL_ORDER_CREATION,
                                 json=data_for_tests.correct_ingredients_for_order_creation, headers=headers)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание заказа без авторизации')
    @allure.description('Проверяем код статуса при создании заказа без авторизации')
    def test_create_order_without_auth(self):
        response = requests.post(data_for_tests.URL_ORDER_CREATION,
                                 json=data_for_tests.correct_ingredients_for_order_creation)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание заказа без ингредиентов')
    @allure.description('Проверяем код статуса при создании заказа без ингредиентов')
    def test_create_order_without_ingredients(self, create_and_login_user_for_order_creation):
        headers = {"Authorization": create_and_login_user_for_order_creation['accessToken']}

        response = requests.post(data_for_tests.URL_ORDER_CREATION, json={"ingredients": []}, headers=headers)

        assert response.status_code == 400 and response.json()["message"] == data_for_tests.ORDER_WITHOUT_INGREDIENT

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    @allure.description('Проверяем код статуса при создании заказа с неверным хешем ингредиентов')
    def test_create_order_with_incorrect_ingredients(self, create_and_login_user_for_order_creation):
        headers = {"Authorization": create_and_login_user_for_order_creation['accessToken']}

        response = requests.post(data_for_tests.URL_ORDER_CREATION,
                                 json=data_for_tests.incorrect_ingredients_for_order_creation, headers=headers)

        assert response.status_code == 500