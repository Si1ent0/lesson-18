from symtable import Class

import allure
from selene import browser, have
from allure_commons.types import AttachmentType
import requests


class Cart:

    def __init__(self):
        self.cookie = None

    @allure.story('Открытие главной страницы')
    def open_main_page(self, cookie):
        with allure.step('Открытие браузера'):
            browser.open('')
        with allure.step('Добавление cookie'):
            browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
        with allure.step('Перезагрузка браузера'):
            browser.driver.refresh()

        return self

    @allure.story('Проверка товаров в корзине')
    def check_add_product(self, item_name):
        with allure.step('Проверка имени товара'):
            browser.element("//a[@href='/cart']/span[@class='cart-label']").click()
            browser.element('.product-name').should(have.text(item_name))

        return self

cart = Cart()