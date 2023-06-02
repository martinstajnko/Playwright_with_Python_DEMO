from time import sleep

from dotenv import dotenv_values
from playwright.sync_api import expect


ENV_VALUES = dotenv_values('secrets.env')

class WooCommerceBackoffice:

    def login_to_backoffice(self, page):
        page.goto(ENV_VALUES['WOOCOMMERCE_BACKOFFICE_URL'])
        page.fill('#user_login', ENV_VALUES['WOOCOMMERCE_BACKOFFICE_USERNAME'])
        page.fill('#user_pass', ENV_VALUES['WOOCOMMERCE_BACKOFFICE_PASSWORD'])
        page.click('#wp-submit')
        expect(page).to_have_title('Dashboard ‹ WeGetFinancing Demo Website — WordPress')
        sleep(0.5)



class WooCommerceStore:

    def add_product_to_cart(self, page):
        page.goto(ENV_VALUES['WOOCOMMERCE_STORE_URL'])
        page.get_by_role("link", name="Shop").click()
        sleep(0.5)
        page.get_by_role("link", name="Add “Macbook Pro m2” to your cart").click()
        sleep(0.5)
        page.get_by_role("link", name="View cart").click()
        sleep(0.5)

    def add_product_to_cart_and_checkout(self, page):
        page.goto(ENV_VALUES['WOOCOMMERCE_STORE_URL'])
        page.get_by_role("link", name="Shop").click()
        sleep(0.5)
        page.get_by_role("link", name="Add “Test Product” to your cart").click()
        sleep(0.5)
        page.get_by_role("link", name="View cart").click()
        sleep(0.5)
        page.get_by_role("link", name="Proceed to checkout").click()
        sleep(0.5)


        textbox_values = [
            ('#billing_first_name', 'Criscel'),
            ('#billing_last_name', 'Stajnko33'),
            ('#billing_company', 'WeGetFinancing'),
            ('#billing_address_1', '123 Main Street'),
            ('#billing_address_2', 'Suite 100'),
            ('#billing_city', 'Los Angeles'),
            ('#billing_postcode', '90017'),
            ('#billing_phone', '1234567890'),
            ('#billing_email', 'criscel@wegetfinancing')
        ]

        for textbox_selector, textbox_value in textbox_values:
            page.fill(textbox_selector, textbox_value)

        page.select_option('#billing_state', 'California')
        page.get_by_role("link", name="WeGetFinancing Checkout Button").click()

        sleep(1)


