from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
from pages.base import BASE_URL
import allure


class CheckoutPage(BasePage):
    CHECKOUT_URL = "/personal/checkout"

    PICKUP_LIST_BUTTON = (
        By.XPATH, "//button[contains(., 'Список')]")

    PICKUP_POINT_SEARCH_INPUT = (
        By.CSS_SELECTOR, "#pickup-points-search-field")

    PICKUP_POINTS_LIST = (By.CSS_SELECTOR, ".delivery-pickup-points-list")

    PICKUP_POINT_ADDRESS = (
        By.CSS_SELECTOR, ".delivery-pickup-point-card__address")

    PICKUP_POINT_ICON = (
        By.CSS_SELECTOR,
        ".delivery-pickup-point-card__selection-icon")

    PICKUP_POINT_BUTTON = (
        By.CSS_SELECTOR,
        ".delivery-pickup-point-card__button-element.button.button--primary")

    RADIO_BUTTON_ICON = (
        By.XPATH, "//label[.//span[@class='radio-button__text' and contains"
                  "(., 'При получении')]]")

    CHECKOUT_BUTTON = (
        By.CSS_SELECTOR, ".checkout-step__button button.button--primary")

    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)
        self.go_to_checkout()

    @allure.step("Переход к оформлению заказа")
    def go_to_checkout(self) -> None:
        self.driver.get(f"{BASE_URL}{self.CHECKOUT_URL}")
        self.wait.until(
            EC.url_contains(self.CHECKOUT_URL)
        )

    @allure.step("Открытие списка пунктов выдачи")
    def open_pickup_list(self) -> None:
        list_button = self.wait.until(
            EC.element_to_be_clickable(self.PICKUP_LIST_BUTTON)
        )
        list_button.click()

    @allure.step("Поиск и выбор пункта выдачи ({address})")
    def search_and_wait_pickup_points(
        self,
        address: str = "г. Самара, Московское шоссе, 205"
    ) -> None:

        with allure.step("Шаг 1: Открываем список пунктов выдачи"):
            self.open_pickup_list()

        with allure.step(f"Шаг 2: Вводим адрес {address}"):
            search_input = self.wait.until(
                EC.element_to_be_clickable(self.PICKUP_POINT_SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(address)

        with allure.step("Шаг 3: Ждем загрузки списка пунктов"):
            self.wait.until(
                EC.visibility_of_element_located(self.PICKUP_POINTS_LIST)
            )

        with allure.step("Шаг 4: Выбираем пункт выдачи"):
            self.select_pickup_point()
            self.click_pickup_button()

    @allure.step("Выбор пункта выдачи")
    def select_pickup_point(self) -> None:
        pickup_icon = self.wait.until(
            EC.element_to_be_clickable(self.PICKUP_POINT_ICON)
        )

        if pickup_icon.is_displayed():
            pickup_icon.click()

    @allure.step("Подтверждение выбора пункта выдачи")
    def click_pickup_button(self) -> None:
        button = self.wait.until(
            EC.element_to_be_clickable(self.PICKUP_POINT_BUTTON)
        )

        if button.is_displayed():
            button.click()

    @allure.step("Выбор способа оплаты при получении")
    def select_radio_button(self) -> None:
        radio_icon = self.wait.until(
            EC.element_to_be_clickable(self.RADIO_BUTTON_ICON)
        )
        if radio_icon.is_displayed():
            radio_icon.click()

    @allure.step("Подтверждение оформления заказа")
    def click_checkout_button(self) -> None:
        button = self.wait.until(
                EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
            )
        button.click()
