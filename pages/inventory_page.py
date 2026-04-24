from playwright.sync_api import expect

class InventoryPage:

    def __init__(self, page):
        self.page = page

    def verify_inventory_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(self.page.locator(".title")).to_have_text("Products")

    def add_first_item_to_cart(self):
        self.page.locator(".inventory_item").first.get_by_role("button", name="Add to cart").click()

    def verify_cart_count(self, count):
        expect(self.page.locator(".shopping_cart_badge")).to_have_text(str(count))