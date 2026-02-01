from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from pages.base import BasePage
import allure


class OrderPage(BasePage):
    ORDER_TITLE = (
        By.CSS_SELECTOR, "h1.order-page__title"
    )
    ORDER_PAGE_URL = "https://shop.mts.ru/personal/order/"

    def __init__(self, driver: Chrome):
        super().__init__(driver)

    @allure.step("Проверяем страницу перехода")
    def is_order_page(self) -> bool:
        current_url: str = self.driver.current_url
        allure.attach(
            f"Текущая URL: {current_url}. "
            f"Ожидаемая URL: {self.ORDER_PAGE_URL}"
        )
        return self.ORDER_PAGE_URL in current_url

    @allure.step("Проверяем заголовок страницы")
    def get_order_title(self) -> str:
        title_element = self.wait.until(
            EC.visibility_of_element_located(self.ORDER_TITLE)
        )
        return title_element.text
