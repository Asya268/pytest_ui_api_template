import pytest
from selenium.webdriver import Chrome
from pages.region import RegionSelectionPage
from pages.action import ActionPage
from pages.base import BASE_URL, REGION
import allure


@pytest.mark.functional
@pytest.mark.ui
@allure.title("Тест проверки актуальных акций")
@allure.story("Полная проверка актуальных акций")
@allure.severity(allure.severity_level.BLOCKER)
def test_full_flow(driver: Chrome):
    """
    Тест полностью проверяет работу с актуальными акциями:
    1. Открытие страницы
    2. Выбор региона
    3. Принятие куки
    4. Переход в раздел акции
    5. Прокрутка страницы
    6. Раскрытие дополнительных акций
    """
    action = ActionPage(driver)
    region_page = RegionSelectionPage(driver)

    with allure.step("Шаг 1. Открытие стартовой страницы"):
        driver.get(BASE_URL)

    with allure.step("Шаг 2. Выбор региона"):
        region_page.select_region(REGION)

    with allure.step("Шаг 3. Принятие куки"):
        action.accept_cookies()

    with allure.step("Шаг 4. Переход к акциям"):
        action.click_actions()
        action.wait_for_actions_url()

    with allure.step("Шаг 5. Открытие дополнительных акций"):
        action.click_show_more()
        action.wait_for_page_2()

    with allure.step("Шаг 6. Проверка загрузки второй страницы акций"):
        assert "page=2" in driver.current_url
