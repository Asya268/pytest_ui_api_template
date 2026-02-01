from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
import allure


class ActionPage(BasePage):
    ACTIONS_BUTTON = (By.CSS_SELECTOR, ".mtsds-tabs__item."
                                       "header-menu__list-item."
                                       "header-menu-list-item")
    SHOW_MORE_BUTTON = (By.CSS_SELECTOR, "div.pagination-new__button-wrapper "
                                         "button.pagination-new__more-button")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход в раздел акции")
    def click_actions(self) -> None:
        with allure.step("Находим и кликаем кнопку акции"):
            actions_button = self.wait.until(
                EC.element_to_be_clickable(self.ACTIONS_BUTTON)
            )
            actions_button.click()

    @allure.step("Ожидание загрузки раздела акций")
    def wait_for_actions_url(self) -> bool:
        return self.wait.until(EC.url_contains("/actions"))

    @allure.step("Открыть дополнительные акции")
    def click_show_more(self) -> None:
        with allure.step("Кликаем кнопку 'Показать еще'"):
            show_more_button = self.find_clickable_element(
                self.SHOW_MORE_BUTTON)
            show_more_button.click()

    @allure.step("Ожидание второй страницы акций")
    def wait_for_page_2(self) -> bool:
        return self.wait.until(
            EC.url_contains("?page=2")
        )
