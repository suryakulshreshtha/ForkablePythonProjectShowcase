"""
Network interception & mocking tests.

Demonstrates: page.route() to mock a response (fulfill) and to block
requests (abort) — testing edge cases without touching the backend.
"""
import json

import pytest
from playwright.sync_api import Page, expect

from utils.config import UI_BASE_URL


@pytest.mark.network
def test_mock_api_response_with_fulfill(page: Page):
    """Intercept an API call and return our own JSON.

    `route.fulfill` short-circuits the request, so the real server is
    never hit — the test is fully deterministic regardless of network.
    """
    mocked = {"data": {"id": 999, "first_name": "Mocked", "last_name": "User"}}

    page.route(
        "**/api/users/2",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(mocked),
        ),
    )

    page.goto("https://reqres.in/")
    result = page.evaluate(
        """async () => {
            const res = await fetch('/api/users/2');
            return await res.json();
        }"""
    )
    assert result["data"]["first_name"] == "Mocked"


@pytest.mark.network
def test_block_images_with_abort(page: Page):
    """Abort all image requests, then prove the app still loads."""
    page.route("**/*.{png,jpg,jpeg,svg,gif}", lambda route: route.abort())
    page.goto(UI_BASE_URL)
    expect(page).to_have_title("Swag Labs")
