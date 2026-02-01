import pytest
from pages.api_client import ApiClient
from typing import Any


@pytest.fixture(scope="session")
def session_api_client() -> Any:
    """
    Фикстура для создания и настройки API
    """
    client = ApiClient()
    yield client
    client.clear_basket()


@pytest.fixture
def api_client(session_api_client: Any) -> Any:
    """
    Фикстура для получения сессии Api
    """
    return session_api_client
