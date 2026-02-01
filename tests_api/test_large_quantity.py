import pytest
import time
from typing import Dict, Any
import allure
from pages.api_client import ApiClient


@pytest.mark.large_data
@allure.title('Корзина')
@allure.story('Добавление большого количества товара')
@allure.severity(allure.severity_level.NORMAL)
def test_add_large_quantity_to_cart(api_client: ApiClient) -> None:
    """
    Тест добавления большого количества товара в корзину
    """
    product_id = 788544
    quantity = 900000

    payload: Dict[str, Any] = {
        "products": [{"quantity": quantity, "id": product_id}],
        "corporate": True
    }

    with allure.step("Шаг 1: Измерение времени выполнения"):
        start_time = time.time()

    with allure.step("Шаг 2: Добавление товара в корзину"):
        response = api_client.add_large_quantity(payload)
        response.raise_for_status()
        data: Dict[str, Any] = response.json()

    with allure.step("Шаг 3: Проверка времени выполнения"):
        assert (
            time.time() - start_time) < 60, "Превышено время обработки (60 с)"

    with allure.step("Шаг 4: Проверка статуса"):
        assert response.status_code == 200

    with allure.step("Шаг 5: Проверка обязательных полей в ответе"):
        assert 'cashback' in data
        required_keys = ['cashback', 'hasSelfRegistrationItem', 'isPreorder']
        assert all(key in data for key in required_keys)

    with allure.step("Шаг 6: Проверка товаров в корзине"):
        assert 'items' in data
        assert len(data['items']) == 1

    with allure.step("Шаг 7: Проверка корректности добавленного товара"):
        item = data['items'][0]
        assert item['id'] == product_id
        assert item['quantity'] == quantity

    with allure.step("Шаг 8: Проверка цены"):
        assert 'price' in data
        assert data['price'] > 0

    with allure.step("Шаг 9: Очистка корзины"):
        api_client.clear_basket()
