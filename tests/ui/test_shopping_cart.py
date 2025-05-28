import allure
from allure_commons.types import Severity

from src.api.shopping_cart import product
from src.ui.cart_page import cart
from data.data import ITEM, ITEM_NAME


@allure.feature("Shopping Cart")
@allure.label("owner", "RS")
@allure.tag("smoke", "regression", "ui", "api" "login")
@allure.severity(Severity.CRITICAL)
@allure.link("https://demowebshop.tricentis.com/cart", name="main page")
@allure.story('Добавление товара в тележку')
def test_add_item_in_cart (ui_url, api_url, login_credentials):
        cookies = product.test_successful_login_api(api_url, login_credentials)
        header = {'Cookie': f'NOPCOMMERCE.AUTH={cookies}'}
        product.add_item(api_url, ITEM, headers=header)
        cart.open_main_page(cookies)
        cart.check_add_product(ITEM_NAME)
