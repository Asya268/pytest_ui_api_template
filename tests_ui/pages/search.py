from pages.base import BasePage
from selenium.webdriver.common.by import By
import allure


class SearchPage(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[name='q']")
    SEARCH_POPUP = (By.ID, "search-popup-field")
    SEARCH_BUTTON = (
        By.CSS_SELECTOR, ".search-popup-result-block__button."
                         "button.button--primary")
    BUY_BUTTON = (By.CSS_SELECTOR, ".product-card-buy-button")

    @allure.step("Выполнение поиска")
    def perform_search(self, query):
        search_field = self.find_clickable_element(self.SEARCH_FIELD)
        search_field.click()

        with allure.step("Ожидание появления попапа поиска"):
            search_popup = self.find_element(self.SEARCH_POPUP)
            search_popup.send_keys(query)

        with allure.step("Клик на кнопку поиска"):
            search_button = self.find_clickable_element(self.SEARCH_BUTTON)
            search_button.send_keys(query)

    @allure.step("Добавление товара в корзину")
    def add_to_basket(self):
        with allure.step("Поиск и клик на кнопку покупки"):
            buy_button = self.find_clickable_element(self.BUY_BUTTON)
            buy_button.click()
