"""
Login flow tests.

Demonstrates: Page Object Model, parametrization across data sets,
and web-first expect() assertions (auto-retry).
"""
import pytest


@pytest.mark.smoke
def test_standard_user_can_login(login_page, credentials):
    user = credentials["users"]["standard"]
    inventory = login_page.login(user["username"], user["password"])
    inventory.expect_loaded()


@pytest.mark.parametrize(
    "user_key, expected_error",
    [
        ("locked_out", "locked out"),
        ("invalid", "Username and password do not match"),
    ],
)
def test_login_failures_show_error(login_page, credentials, user_key, expected_error):
    user = credentials["users"][user_key]
    login_page.login(user["username"], user["password"])
    login_page.expect_error(expected_error)
