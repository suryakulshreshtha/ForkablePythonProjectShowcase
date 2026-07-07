"""Base page object with helpers shared by every page."""
from playwright.sync_api import Page


class BasePage:
    """Parent for all page objects. Holds the Playwright `page` and common helpers."""

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        """Navigate to an absolute URL."""
        self.page.goto(url)

    def title(self) -> str:
        return self.page.title()
