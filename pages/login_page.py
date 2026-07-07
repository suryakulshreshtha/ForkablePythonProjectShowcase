"""Login page object for saucedemo.com."""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from utils.config import UI_BASE_URL


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Semantic locators first: placeholders + role.
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        # The error banner has no role/label, so we fall back to a stable test id.
        self.error_message = page.locator('[data-test="error"]')

    def load(self) -> "LoginPage":
        self.open(UI_BASE_URL)
        return self

    def login(self, username: str, password: str) -> InventoryPage:
        """Perform login and return the next page object (fluent pattern)."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return InventoryPage(self.page)

    def expect_error(self, text: str):
        """Web-first assertion: auto-retries until the banner shows `text`."""
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(text)
