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

    pass
