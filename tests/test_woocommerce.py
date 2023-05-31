import pytest
from dotenv import dotenv_values
from playwright.sync_api import sync_playwright, Page

from functions import WooCommerceBackoffice


@pytest.fixture(autouse=True)
def page():
    with sync_playwright() as playwright:
        env_values = dotenv_values('secrets.env')
        browser = playwright.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()
        page.goto(env_values['WOOCOMMERCE_BACKOFFICE_URL'])
        yield page
        page.close()
        context.close()
        browser.close()


class TestWooCommerceBackoffice:

    def test_login(self, page: Page) -> None:
        WooCommerceBackoffice().login_to_backoffice(page)



class TestWooCommerceE2E:

    def test_e2e_process(self, page: Page) -> None:
        pass


    



