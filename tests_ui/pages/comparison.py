from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from pages.base import BasePage
import allure


class ComparisonPage(BasePage):
    SEARCH_QUERY = "Смартфон Apple iPhone 17 Pro Max 512 Гб eSIM + " \
                   "SIM Cosmic Orange"
    NEW_SEARCH_QUERY = "Смартфон Apple iPhone 17 256 Гб eSIM + SIM Lavender"

    COMPARE_BUTTON = (
        By.CSS_SELECTOR,
        "button.product-card-compare-button"
    )

    PRODUCT_NAMES = (
        By.CSS_SELECTOR,
        ".compare-product-card__title-link .compare-product-card__title"
    )

    COMPARE_URL = "https://shop.mts.ru/compare/?ids=946980,947520"

    def __init__(self, driver):
        super().__init__(driver)

    def find_elements(self, locator, timeout=10) -> List[WebElement]:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Добавление товара в сравнение")
    def add_product_to_comparison(self) -> None:
        compare_button = self.find_clickable_element(self.COMPARE_BUTTON)
        compare_button.click()

    @allure.step("Проверка количества товаров в сравнении")
    def check_products_in_comparison(self) -> None:
        product_elements = self.find_elements(self.PRODUCT_NAMES)
        assert len(product_elements) == 2, "В сравнении должно быть 2 товара"

    @allure.step("Проверка количества товаров")
    def check_products_count(self, expected_count: int) -> None:
        product_elements = self.find_elements(self.PRODUCT_NAMES)
        assert len(product_elements) == expected_count, (
            f"Ожидалось {expected_count} товаров, найдено: {len(
                product_elements)}"
        )

    @allure.step("Переход на страницу сравнения")
    def go_to_comparison_page(self) -> None:
        self.driver.get(self.COMPARE_URL)

    @property
    def get_search_query(self) -> str:
        return self.SEARCH_QUERY

    @property
    def get_new_search_query(self) -> str:
        return self.NEW_SEARCH_QUERY
