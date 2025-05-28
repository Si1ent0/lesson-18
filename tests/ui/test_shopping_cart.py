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
        cookie = product.add_item(api_url, ITEM)
        cart.open_main_page(cookie)
        cart.check_add_product(ITEM_NAME)
