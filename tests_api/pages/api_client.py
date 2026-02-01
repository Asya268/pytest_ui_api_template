from typing import Dict, Optional
import allure
import requests
from requests import Response
import os


class ApiClient:
    def __init__(self, base_url: str = 'https://shop.mts.ru/api/v1'):
        self.base_url = base_url
        self.auth_token = os.getenv('MTS_AUTH_TOKEN')
        self.session = requests.Session()
        self.setup_session()

    @allure.step("Настройка сессии API")
    def setup_session(self):
        """
        Инициализация сессии с необходимыми хедерами и куки
        """
        self.session.headers.update(self.get_auth_headers())
        self.session.cookies.update(self.get_cookies())

    @allure.step("Получение хедеров авторизации")
    def get_auth_headers(self) -> Dict[str, str]:
        """
        Формирование хедеров для авторизации
        """
        return {
            'Authorization-JWT': f'Bearer {self.auth_token}',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        }

    @allure.step("Получение куки")
    def get_cookies(self) -> Dict[str, str]:
        """
        Получение необходимых куки
        """
        return {}

    @allure.step("Поиск товаров")
    def search_products(
        self,
        params: Optional[Dict] = None,
        search_url: str = 'https://shop.mts.ru/apigw/api/v1/search/hits'
    ) -> requests.Response:
        """
        Поиск товаров по заданным параметрам

        """
        return self.session.get(search_url, params=params)

    @allure.step("Добавление товара в корзину")
    def add_to_cart(
        self,
        product_data: Dict,
        add_url: str = '/cart/add'
    ) -> Response:
        full_url = f"{self.base_url}{add_url}"
        return self.session.post(full_url, json=product_data)

    @allure.step("Удаление товара из корзины")
    def delete_from_cart(
        self,
        item_id: str,
        delete_url: str = '/baskets/current/items/'
    ) -> requests.Response:
        full_url = f"{self.base_url}{delete_url}{item_id}?corporate=false"
        return self.session.delete(full_url)

    @allure.step("Добавление большого количества товара")
    def add_large_quantity(
        self,
        payload: Dict,
        url: str = '/baskets/current/items'
    ) -> requests.Response:
        full_url = f"{self.base_url}{url}"
        return self.session.patch(full_url, json=payload)

    @allure.step("Очистка корзины")
    def clear_basket(
        self,
        clear_url: str = '/baskets/current/items'
    ) -> Response:
        full_url = f"{self.base_url}{clear_url}"
        return self.session.delete(full_url)

    @allure.step("Оформление заказа")
    def place_order(
        self,
        order_data: Dict,
        order_url: str = '/orders'
    ) -> Response:
        full_url = f"{self.base_url}{order_url}"
        return self.session.post(full_url, json=order_data)

    @allure.step("Получение информации о корзине")
    def get_basket(
        self,
        basket_url: str = '/baskets/current'
    ) -> Response:
        full_url = f"{self.base_url}{basket_url}"
        return self.session.get(full_url)
