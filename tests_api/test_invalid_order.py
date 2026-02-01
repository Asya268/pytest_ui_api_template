import pytest
import allure
from pages.api_client import ApiClient


@pytest.mark.negative
@allure.title('Оформление заказа')
@allure.story('Невалидный адрес доставки')
@allure.severity(allure.severity_level.NORMAL)
def test_order_with_invalid_address(api_client: ApiClient) -> None:
    """
    Тест проверяет поведение системы при попытке оформления заказа
    с некорректным адресом
    """
    with allure.step("Формирование данных заказа с некорректным адресом"):
        order_data = {
            "delivery": {
                "address": {
                    "country": "Россия",
                    "region": "Не существующий регион",
                    "city": "Не существующий город",
                    "street": "Не существующая улица",
                    "house": "1234567890",
                    "flat": "1"
                },
                "type": "курьер"
            },
            "payment": {
                "type": "card"
            }
        }

    with allure.step("Шаг 1: Попытка оформления заказа"):
        response = api_client.place_order(order_data)

    with allure.step("Шаг 2: Проверяем статус кода"):
        assert response.status_code == 404

    with allure.step("Шаг 3: Проверка структуры ответа об ошибке"):
        response_data = response.json()
        error_data = response_data.get('error', {})

    with allure.step("Шаг 4: Проверка поля ошибки"):
        assert error_data.get('code') == 404
        assert error_data.get('title') == '404 Not Found'
        assert isinstance(error_data.get('details'), list)
