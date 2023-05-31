from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input_selector = "#username"
        self.password_input_selector = "#password"
        self.login_button_selector = "#login-button"

    def enter_credentials(self, username, password):
        username_input = self.find_element(self.username_input_selector)
        password_input = self.find_element(self.password_input_selector)
        username_input.fill(username)
        password_input.fill(password)

    def submit_login_form(self):
        login_button = self.find_element(self.login_button_selector)
        login_button.click()

    def login(self, username, password):
        self.navigate_to("/login")
        self.enter_credentials(username, password)
        self.submit_login_form()

    # Other login-related methods...
