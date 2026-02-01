import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.region import RegionSelectionPage
from pages.search import SearchPage
from pages.basket import BasketPage
from pages.checkout import CheckoutPage
from pages.recipient import RecipientPage
from pages.order import OrderPage
from selenium.webdriver import Chrome
from pages.base import BASE_URL, REGION
import allure


@pytest.mark.functional
@pytest.mark.ui
@allure.title("Тест полного процесса покупки")
@allure.story("Проверка  процесса оформления заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_full_purchase_process(driver: Chrome,
                               product_name, recipient_data) -> None:
    """
    Тест проверяет процесс покупки от начала до конца:
    1. Открытие страницы
    2. Выбор региона
    3. Принятие куки
    4. Поиск товара
    6. Добавление товара в корзину
    7. Оформление товара
    8. Оформление самовывоза
    9. Заполнение данных получателя
    10. Проверка оформления заказа
    """
    with allure.step("Шаг 1: Открытие стартовой страницы"):
        driver.get(BASE_URL)
        region_page = RegionSelectionPage(driver)
        search_page = SearchPage(driver)

    with allure.step("Шаг 2: Выбор региона"):
        region_page.select_region(REGION)

    with allure.step("Шаг 3: Принятие куки"):
        search_page.accept_cookies()

    with allure.step("Шаг 4: Поиск товара"):
        search_page.perform_search(product_name)

    with allure.step("Шаг 5: Переход в корзину"):
        search_page.add_to_basket()
        basket_page = BasketPage(driver)

        # Простая проверка суммы заказа
        with allure.step("Проверка общей суммы заказа"):
            total_price = basket_page.get_total_price()
            allure.attach(f"Полученная сумма: {total_price}",
                          name="Проверка суммы")

            # Минимальная валидация: сумма не пустая и содержит цифры
            assert total_price, "Сумма заказа не должна быть пустой"
            assert any(char.isdigit() for char in total_price), \
                "Сумма заказа должна содержать цифры"

        basket_page.agree_to_terms()
        basket_page.proceed_to_checkout()

    with allure.step("Шаг 6: Оформление самовывоза"):
        checkout_page = CheckoutPage(driver)
        checkout_page.search_and_wait_pickup_points()
        checkout_page.select_radio_button()
        checkout_page.click_checkout_button()

    with allure.step("Шаг 7: Переход на страницу данных получателя"):
        recipient_page = RecipientPage(driver)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(RecipientPage.FIRST_NAME_INPUT))
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(RecipientPage.FIRST_NAME_INPUT))
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(RecipientPage.FIRST_NAME_INPUT))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Шаг 8: Заполнение данных получателя"):
        recipient_page.fill_recipient_info(
            first_name=recipient_data["first_name"],
            last_name=recipient_data["last_name"],
            phone=recipient_data["phone"],
            email=recipient_data["email"]
        )
        recipient_page.click_submit_button()

    with allure.step("Шаг 9: Проверка перехода на страницу заказа"):
        order_page = OrderPage(driver)

        WebDriverWait(driver, 30).until(
            lambda driver: order_page.ORDER_PAGE_URL in driver.current_url)
    assert order_page.is_order_page()
    order_title = order_page.get_order_title()
    assert "оформлен" in order_title.lower()
