import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.addresses import AddressesPage
from pages.region import RegionSelectionPage
from pages.base import BASE_URL, REGION
import allure


@pytest.mark.functional
@pytest.mark.ui
@allure.title("Тест проверки адресов магазинов")
@allure.story("Работа с адресами магазинов")
@allure.severity(allure.severity_level.NORMAL)
def test_check_addresses(driver: WebDriver) -> None:
    """
    Тест проверяет работу списка адресов магазинов:
    1. Открытие страницы
    2. Выбор региона
    3. Принятие куки
    4. Переход в раздел адреса магазинов
    """
    with allure.step("Шаг 1: Открытие стартовой страницы"):
        driver.get(BASE_URL)
    with allure.step("Шаг 2: Выбор региона"):
        region_page = RegionSelectionPage(driver)
        region_page.select_region(REGION)
    with allure.step("Шаг 3: Загрузка страницы адресов"):
        main = AddressesPage(driver)
        main.accept_cookies()
        main.open_more_menu()
        main.go_to_addresses()
    with allure.step("Шаг 4: Проверка заголовка страницы"):
        main.check_addresses_page_title()
