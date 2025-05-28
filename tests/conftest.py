import pytest
from selene import browser
from utils import attach

@pytest.fixture(scope="function", autouse=True)
def browser_setting():
    browser.config.base_url = 'https://demowebshop.tricentis.com/cart'
    browser.config.window_height = 1800
    browser.config.window_width = 1200

    yield browser

    attach.add_logs(browser)

    browser.quit()

@pytest.fixture
def api_url():
    return 'https://demowebshop.tricentis.com/'


@pytest.fixture
def ui_url():
    return 'https://demowebshop.tricentis.com/'


@pytest.fixture
def headers():
    headers = {
        "x-api-key": "reqres-free-v1"}
    return headers


@pytest.fixture(params=[
    ("example1200@example.com", "123456")
])
def login_credentials(request):
    return request.param
