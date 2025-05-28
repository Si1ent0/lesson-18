import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType


class Product:
    @allure.step("API. Проверка успешной авторизации.")
    def test_successful_login_api(self, api_url, login_credentials):
        username, password = login_credentials
        """Successful authorization to some demowebshop (API)"""
        with step("Login with API"):
            result = requests.post(
                url=api_url + "/login",
                data={"Email": username, "Password": password, "RememberMe": False},
                allow_redirects=False
            )
            allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT,
                          extension="txt")
        with step("Get cookie from API"):
            self.cookie = result.cookies.get("NOPCOMMERCE.AUTH")

        return self.cookie

    @allure.story('Добавление items в тележку')
    def add_item(self, api_url, item_id, headers):

        url = api_url + '/addproducttocart/catalog/' + item_id
        with allure.step('Добавление item в тележку'):
            response = requests.post(url, headers=headers)
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        with allure.step('Проверка кода'):
            assert response.status_code == 200

        return response.cookies.get("NOPCOMMERCE.AUTH")


product = Product()