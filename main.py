from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://partner.sandbox.wegetfinancing.com/')
    page.fill('#id_username', 'martin.stajnko')
    page.fill('#id_password', 'ohwoolu3Shei')
    page.click('input[type="submit"]')
    print(page.title())
    browser.close()