"""Inventory (products) page object for saucedemo.com."""
import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.app_logo = page.locator(".app_logo")          # "Swag Labs"
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')

    def expect_loaded(self):
        """Confirm we actually landed on the inventory page after login."""
        expect(self.page).to_have_url(re.compile(r"inventory"))
        expect(self.app_logo).to_have_text("Swag Labs")

    def add_item_to_cart(self, product_name: str):
        """Find a product card by its name (filter), then click its Add button."""
        card = self.inventory_items.filter(has_text=product_name)
        card.get_by_role("button", name="Add to cart").click()

    def cart_count(self) -> int:
        """Number shown on the cart badge (0 when hidden)."""
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def sort_by(self, option_value: str):
        """option_value: 'az' | 'za' | 'lohi' | 'hilo'."""
        self.sort_dropdown.select_option(option_value)

    def product_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_inner_texts()
