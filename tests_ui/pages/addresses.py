from selenium.webdriver.common.by import By
from pages.base import BasePage
import allure


class AddressesPage(BasePage):
    MORE_BUTTON = (By.XPATH, "//button[contains(@class, "
                             "'pre-header-content__button') "
                             "and contains(text(), 'Ещё')]")
    ADDRESSES_LINK = (By.XPATH, "//label[contains(., 'Адреса магазинов')]")
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.mdsx-page-heading__header")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход в раздел 'Еще'")
    def open_more_menu(self) -> None:
        self.find_clickable_element(self.MORE_BUTTON).click()

    @allure.step("Переход в раздел адресов")
    def go_to_addresses(self) -> None:
        self.find_clickable_element(self.ADDRESSES_LINK).click()

    @allure.step("Проверка заголовка страницы")
    def check_addresses_page_title(self) -> None:
        with allure.step("Проверяем заголовок страницы"):
            title_element = self.find_element(self.PAGE_TITLE)
            assert title_element.text == "Адреса магазинов в г. Самара"
