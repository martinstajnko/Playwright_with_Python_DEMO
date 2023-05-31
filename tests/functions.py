from time import sleep

from dotenv import dotenv_values
from playwright.sync_api import expect

class WooCommerceBackoffice:

    env_values = dotenv_values('secrets.env')

    def login_to_backoffice(self, page):
        page.goto(self.env_values['WOOCOMMERCE_BACKOFFICE_URL'])
        page.fill('#user_login', self.env_values['WOOCOMMERCE_BACKOFFICE_USERNAME'])
        page.fill('#user_pass', self.env_values['WOOCOMMERCE_BACKOFFICE_PASSWORD'])
        page.click('#wp-submit')
        expect(page).to_have_title('Dashboard ‹ WeGetFinancing Demo Website — WordPress')
        sleep(0.5)