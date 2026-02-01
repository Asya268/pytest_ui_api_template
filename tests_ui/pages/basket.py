from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BASE_URL
import allure


class BasketPage(BasePage):
    BASKET_URL = "/personal/basket"

    AGREE_BUTTON = (
        By.CSS_SELECTOR, ".checkbox__place-icon")
    PROCEED_BUTTON = (
        By.CSS_SELECTOR, ".basket-promo-info__button.button.button--primary")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".purchase-info__total-sum")

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_basket()

    @allure.step("Переходим в корзину")
    def go_to_basket(self):
        self.driver.get(f"{BASE_URL}{self.BASKET_URL}")

    @allure.step("Соглашаемся с условиями начисления")
    def agree_to_terms(self) -> None:
        agree_button = self.find_clickable_element(self.AGREE_BUTTON)
        agree_button.click()

    @allure.step("Переходим к оформлению заказа")
    def proceed_to_checkout(self) -> None:
        proceed_button = self.find_clickable_element(self.PROCEED_BUTTON)
        proceed_button.click()

    @allure.step("Получаем общую сумму заказа")
    def get_total_price(self) -> str:
        """"Находим элемент и сразу получаем текст"""
        total_price = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_PRICE)
        ).text.strip()

        """Сохраняем в Allure"""
        allure.attach(f"Общая сумма заказа: {total_price}",
                      name="Сумма заказа")

        return total_price
