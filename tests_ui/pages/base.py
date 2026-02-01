from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import allure

BASE_URL = "https://shop.mts.ru/"
REGION = "Самара"


class BasePage:
    COOKIES_BUTTON = (By.CLASS_NAME, "cookies-massage__btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Поиск и клик на элемент")
    def find_element(self, locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Шаг 2: Принятие куки")
    def accept_cookies(self) -> None:
        with allure.step("Кликаем кнопку принятия куки"):
            self.find_clickable_element(self.COOKIES_BUTTON).click()
