import pytest
from pages.api_client import ApiClient
import allure
from typing import Any, Dict, List, Tuple

SEARCH_CASES: List[Tuple[str, bool]] = [
    ("iphone", True)
]


@pytest.mark.parametrize("search_query, expect_results", SEARCH_CASES)
@allure.title('Поиск товаров')
@allure.story('Базовый поиск')
@allure.severity(allure.severity_level.NORMAL)
def test_get_products(api_client: ApiClient,
                      search_query: str, expect_results: bool) -> None:
    """
    Тест проверяет поиск товара
    """
    params = {
        'st': search_query,
        'project': 'shop',
        'platform': 'web',
        'strategy': 'advanced_xname,zero_queries',
        'regionId': "77000000000000000000000000",
        'showUnavailable': True
    }
    with allure.step("Шаг 1: Выполнение поиска товаров"):
        response = api_client.search_products(params)
        response.raise_for_status()

    with allure.step("Шаг 2: Проверка статус ответа"):
        assert response.status_code == 200

    with allure.step("Шаг 3: Проверка структуру ответа"):
        data: Dict[str, Any] = response.json()
        assert 'success_response' in data

    with allure.step("Шаг 4: Проверка наличие товаров"):
        assert len(data['success_response']['hits']) > 0
