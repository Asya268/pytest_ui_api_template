from selenium.webdriver.common.by import By
from pages.base import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


class RecipientPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "user-firstname")
    LAST_NAME_INPUT = (By.ID, "user-lastname")
    PHONE_INPUT = (By.ID, "user-phone")
    EMAIL_INPUT = (By.ID, "user-email")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".button.button--primary")

    @allure.step("Ожидание загрузки страницы получателя")
    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        )
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
        )

    @allure.step("Заполнение информации о получателе")
    def fill_recipient_info(
            self, first_name, last_name, phone, email) -> None:
        with allure.step("Заполнение поля имени"):
            self.wait.until(
                EC.presence_of_element_located(
                    self.FIRST_NAME_INPUT)).send_keys(first_name)

        with allure.step("Заполнение поля фамилии"):
            self.wait.until(
                EC.presence_of_element_located(
                    self.LAST_NAME_INPUT)).send_keys(last_name)

        with allure.step("Заполнение поля телефона"):
            self.wait.until(
                EC.presence_of_element_located(
                    self.PHONE_INPUT)).send_keys(phone)

        with allure.step("Заполнение поля email"):
            self.wait.until(
                EC.presence_of_element_located(
                    self.EMAIL_INPUT)).send_keys(email)    

    @allure.step("Отправка формы")
    def click_submit_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        button.click()
