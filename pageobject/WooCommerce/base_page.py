class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://example.com"  # Replace with the actual base URL of your WooCommerce store

    def navigate_to(self, path):
        url = self.base_url + path
        self.page.goto(url)

    def find_element(self, selector):
        return self.page.query_selector(selector)

    # Other common methods...
