from playwright.sync_api import sync_playwright

def test_without_login(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()

    page.goto("https://www.saucedemo.com/inventory.html")

    assert "inventory" in page.url