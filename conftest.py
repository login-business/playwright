import pytest

@pytest.fixture
def login_page(page):
    from pages.login_page import LoginPage

    login = LoginPage(page)
    login.navigate()
    return login