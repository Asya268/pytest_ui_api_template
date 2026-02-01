import pytest
from pages.api_client import ApiClient
import allure
from requests import Response


@pytest.mark.functional
@allure.title('Корзина')
@allure.story('Добавление товара в корзину')
@allure.severity(allure.severity_level.NORMAL)
def test_add_to_cart(api_client: ApiClient) -> None:
    """
    Тест проверяет процесс добавления товара в корзину

    """
    product_data = {
        "id": "946962",
        "quantity": 1
    }

    with allure.step("Шаг 1:Добавление товара {product_id} "
                     "в количестве {quantity}"):
        response: Response = api_client.add_to_cart(product_data)
        response.raise_for_status()
        data = response.json()

    with allure.step("Шаг 2: Проверка статуса"):
        assert response.status_code == 200
    with allure.step("Шаг 3: Проверка SALE_UID"):
        assert 'SALE_UID' in data
    with allure.step("Шаг 4: Проверка ключа"):
        assert 'personalCart' in data
    with allure.step("Шаг 5: Проверка товаров в корзине"):
        assert len(data['personalCart']['items']) > 0
        item = data['personalCart']['items'][0]
    with allure.step("Шаг 6: Проверка корректности добавленного товара"):
        assert item['id'] == int(product_data['id'])
        assert item['quantity'] == product_data['quantity']
