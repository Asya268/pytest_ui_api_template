import pytest
from pages.api_client import ApiClient
import allure


@allure.title('Корзина')
@allure.story('Удаление товара из корзины')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.functional
def test_delete_from_cart(api_client: ApiClient,) -> None:
    """
    Тест проверяет возможность удаления товара из корзины

    """
    product_data = {
        "id": "946962",
        "quantity": 1
    }

    with allure.step("Шаг 1: Добавление товара в корзину"):
        add_response = api_client.add_to_cart(product_data)
        add_response.raise_for_status()
        add_data = add_response.json()

    with allure.step("Шаг 2: Получение ID товара"):
        item_id = add_data['personalCart']['items'][0]['cartItemId']

    with allure.step("Шаг 3: Удаление товара из корзины"):
        delete_response = api_client.delete_from_cart(item_id)
        delete_response.raise_for_status()
        data = delete_response.json()

    with allure.step("Шаг 4: Проверка состояния корзины"):
        assert data.get('personalCart', {}).get('items', []) == []
        assert data.get('price', 0) == 0
