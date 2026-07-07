"""
Shared fixtures, auto-discovered by every test (no imports needed).

`pytest-playwright` already provides `page`, `context`, `browser`,
`browser_type`, and `playwright` fixtures, so we only add what's
specific to this project.
"""
import json
from pathlib import Path

import pytest
from playwright.sync_api import Page, Playwright

from pages.login_page import LoginPage
from utils.api_utils import BookingAPI
from utils.config import API_BASE_URL

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture(scope="session")
def credentials() -> dict:
    """Load external test data once per session."""
    with open(DATA_DIR / "credentials.json") as f:
        return json.load(f)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """A LoginPage already navigated to the app."""
    return LoginPage(page).load()


@pytest.fixture
def standard_user_inventory(login_page: LoginPage, credentials: dict):
    """Logs in as the standard user and returns the InventoryPage.

    Demonstrates reusing a page-object flow as a fixture so individual
    tests don't repeat the login steps.
    """
    user = credentials["users"]["standard"]
    inventory = login_page.login(user["username"], user["password"])
    inventory.expect_loaded()
    return inventory


@pytest.fixture
def booking_api(playwright: Playwright) -> BookingAPI:
    """An APIRequestContext wrapped in our BookingAPI helper."""
    request_context = playwright.request.new_context(
        base_url=API_BASE_URL,
        extra_http_headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    yield BookingAPI(request_context)   # setup done; test runs here
    request_context.dispose()           # teardown
