from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class RegionSelectionPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    REGION_BUTTON = (By.CSS_SELECTOR, ".confirm-region__btn--rejection")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    CITY_BUTTON = (By.XPATH, "//button[contains(text(), 'Самара')]")

    @allure.step("Шаг 1: Клик по кнопке выбора региона")
    def click_region_button(self) -> None:
        with allure.step("Кликаем по кнопке выбора региона"):
            button = self.wait.until(
                EC.element_to_be_clickable(self.REGION_BUTTON))
            button.click()

    @allure.step("Шаг 2: Ввод города в поисковую строку")
    def input_city(self, city_name: str) -> None:
        with allure.step(f"Вводим город: {city_name}"):
            input_field = self.wait.until(
                EC.element_to_be_clickable(self.SEARCH_INPUT))
            input_field.clear()
            input_field.send_keys(city_name)

    @allure.step("Шаг 3. Выбор города из списка")
    def select_city(self) -> None:
        with allure.step("Клик по кнопке выбранного города"):
            city_btn = self.wait.until(
                EC.element_to_be_clickable(self.CITY_BUTTON))
            city_btn.click()

    @allure.step("Полный сценарий выбора региона")
    def select_region(self, city_name: str = "Самара") -> None:
        with allure.step(f"Выбираем регион для города: {city_name}"):
            self.click_region_button()
            self.input_city(city_name)
            self.select_city()
