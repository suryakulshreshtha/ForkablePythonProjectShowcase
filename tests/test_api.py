"""
API tests against the restful-booker practice API.

Demonstrates: Playwright's built-in APIRequestContext, a reusable API
utility layer, token authentication, and status-code / JSON assertions.
"""
import pytest


@pytest.mark.api
def test_create_and_fetch_booking(booking_api):
    # 1. Create a booking via POST.
    payload = booking_api.sample_payload()
    create_resp = booking_api.create_booking(payload)
    assert create_resp.status == 200

    body = create_resp.json()
    booking_id = body["bookingid"]
    assert body["booking"]["firstname"] == payload["firstname"]

    # 2. Fetch it back via GET and verify it matches.
    get_resp = booking_api.get_booking(booking_id)
    assert get_resp.ok
    fetched = get_resp.json()
    assert fetched["lastname"] == payload["lastname"]
    assert fetched["totalprice"] == payload["totalprice"]


@pytest.mark.api
def test_auth_returns_token(booking_api):
    token = booking_api.create_token("admin", "password123")
    assert token and isinstance(token, str)
