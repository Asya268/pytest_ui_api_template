from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
import allure


class CatalogPage(BasePage):
    CATALOG_BUTTON = (By.CSS_SELECTOR, "button.catalog-button")
    MERCH_SECTION = (By.XPATH, "//a[@href='/catalog/merch/']")
    MERCH_HEADER = (By.CSS_SELECTOR, ".mdsx-page-heading__header")
    MERCH_URL = "https://shop.mts.ru/catalog/merch/"

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть каталог")
    def open_catalog(self) -> None:
        catalog_button = self.wait.until(
            EC.element_to_be_clickable(self.CATALOG_BUTTON)
        )
        catalog_button.click()

    @allure.step("Переход в раздел 'Мерч'")
    def go_to_merch(self) -> None:
        merch_button = self.wait.until(
            EC.element_to_be_clickable(self.MERCH_SECTION)
        )
        merch_button.click()

    @allure.step("Проверка заголовка страницы")
    def get_merch_header_text(self) -> str:
        header = self.wait.until(
            EC.visibility_of_element_located(self.MERCH_HEADER))
        return header.text.strip()
