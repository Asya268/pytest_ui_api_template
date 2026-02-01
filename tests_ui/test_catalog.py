import pytest
from selenium.webdriver import Chrome
from pages.region import RegionSelectionPage
from pages.base import BASE_URL, REGION
from pages.catalog import CatalogPage
import allure


@pytest.mark.functional
@pytest.mark.ui
@allure.title("Тест проверки работы раздела")
@allure.story("Работа с категорией товара")
@allure.severity(allure.severity_level.NORMAL)
def test_search_merch_product(driver: Chrome) -> None:
    """
    Тест проверяет работу списка адресов магазинов:
    1. Открытие страницы
    2. Выбор региона
    3. Принятие куки
    4. Переход в каталог
    6. Переход в раздел мерч
    """
    catalog = CatalogPage(driver)
    with allure.step("Шаг 1: Открытие стартовой страницы"):
        driver.get(BASE_URL)

    with allure.step("Шаг 2: Выбор региона"):
        region_page = RegionSelectionPage(driver)
        region_page.select_region(REGION)

    with allure.step("Шаг 3. Принятие куки"):
        catalog.accept_cookies()

    with allure.step("Шаг 4: Открытие каталога"):
        catalog.open_catalog()

    with allure.step("Шаг 5: Переход в раздел 'Мерч'"):
        catalog.go_to_merch()

    with allure.step("Шаг 6: Проверка URL раздела"):
        assert driver.current_url == catalog.MERCH_URL

    with allure.step("Шаг 7: Проверка заголовка раздела"):
        header_text = catalog.get_merch_header_text()
        assert "Мерч МТС" in header_text, (
            "Неверный заголовок раздела: "
            f"{header_text}")
