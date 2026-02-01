import pytest
from selenium.webdriver import Chrome
from pages.region import RegionSelectionPage
from pages.comparison import ComparisonPage
from pages.search import SearchPage
from pages.base import BASE_URL, REGION
import allure


@pytest.mark.functional
@pytest.mark.ui
@allure.title("Тест сравнения товаров")
@allure.story("Добавление товаров в сравнение")
@allure.severity(allure.severity_level.NORMAL)
def test_comparison(driver: Chrome):
    """
    Тест проверяет функционал сравнения товаров:
    1. Добавление первого товара в сравнение
    2. Добавление второго товара в сравнение
    3. Проверка корректности сравнения
    """
    comparison_page = ComparisonPage(driver)

    with allure.step("Шаг 1: Открытие стартовой страницы"):
        driver.get(BASE_URL)

    with allure.step("Шаг 2: Выбор региона"):
        region_page = RegionSelectionPage(driver)
        region_page.select_region(REGION)

    with allure.step("Шаг 3: Принятие куки"):
        comparison_page.accept_cookies()

    with allure.step("Шаг 4: Поиск и добавление первого товара"):
        search_page = SearchPage(driver)
        search_page.perform_search(comparison_page.get_search_query)
        comparison_page.add_product_to_comparison()

    with allure.step("Шаг 5: Поиск и добавление второго товара"):
        driver.back()
        search_page.perform_search(comparison_page.get_new_search_query)
        comparison_page.add_product_to_comparison()

    with allure.step("Шаг 6: Переход на страницу сравнения"):
        comparison_page.go_to_comparison_page()

    with allure.step("Шаг 7: Проверка результатов сравнения"):
        comparison_page.check_products_in_comparison()
        comparison_page.check_products_count(2)
