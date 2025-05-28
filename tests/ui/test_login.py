import allure
from allure_commons._allure import step
from allure_commons.types import Severity
from selene import browser, have
from src.api.shopping_cart import product


@allure.feature("Login")
@allure.label("owner", "RS")
@allure.tag("smoke", "regression", "ui", "login")
@allure.severity(Severity.CRITICAL)
@allure.link("https://demowebshop.tricentis.com/", name="main page")
@allure.step("UI. Проверка успешной авторизации с username и password.")
def test_successful_login_ui(ui_url, login_credentials):
    username, password = login_credentials
    """Successful authorization to some demowebshop (UI)"""
    with step("Open login page"):
        browser.open("http://demowebshop.tricentis.com/login")

    with step("Fill login form"):
        browser.element("#Email").send_keys(username)
        browser.element("#Password").send_keys(password).press_enter()

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(username))

@allure.feature("Login")
@allure.label("owner", "RS")
@allure.tag("smoke", "regression", "ui", "login")
@allure.severity(Severity.CRITICAL)
@allure.link("https://demowebshop.tricentis.com/", name="main page")
@allure.step("UI. Проверка успешной авторизации c куками.")
def test_login_with_set_cookie(ui_url, api_url, login_credentials):
    cookie = product.test_successful_login_api(api_url, login_credentials)
    with step("Set cookie from API"):
        username, password = login_credentials
        browser.open(ui_url)
        # Применение кук из api
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        # Повторное открытие браузера, для применения переданной куки
        browser.open(ui_url)

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(username))
