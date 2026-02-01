import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import allure

PRODUCT_NAME = "Смартфон HONOR X6C 6/128 Гб LTE Полночный черный"
RECIPIENT_DATA = {
    "first_name": "Анастасия",
    "last_name": "Жилина",
    "phone": "+79997775544",
    "email": "80v77@virgilian.com"
}


@pytest.fixture
def product_name():
    """Фикстура для имени продукта"""
    return PRODUCT_NAME


@pytest.fixture
def recipient_data():
    """Фикстура для данных получателя"""
    return RECIPIENT_DATA


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для настройки и управления веб-драйвером Chrome
    """
    with allure.step("Настройка драйвера"):
        options = Options()
        options.add_experimental_option(
            "prefs",
            {
                "profile.default_content_setting_values.notifications": 2
            }
        )

    with allure.step("Инициализация драйвера"):
        driver = Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    with allure.step("Раскрытие окна"):
        driver.maximize_window()

    yield driver

    with allure.step("Закрытие браузера"):
        driver.quit()
