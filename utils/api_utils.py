"""
API utility layer for the restful-booker practice API.

Wraps the raw HTTP calls so tests read at the business level
(create_token, create_booking, get_booking) instead of dealing
with URLs and payloads directly.
"""
from playwright.sync_api import APIRequestContext, APIResponse


class BookingAPI:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def create_token(self, username: str, password: str) -> str:
        resp = self.request.post(
            "/auth", data={"username": username, "password": password}
        )
        assert resp.ok, f"Auth failed: {resp.status}"
        return resp.json()["token"]

    def create_booking(self, payload: dict) -> APIResponse:
        return self.request.post("/booking", data=payload)

    def get_booking(self, booking_id: int) -> APIResponse:
        return self.request.get(f"/booking/{booking_id}")

    @staticmethod
    def sample_payload() -> dict:
        return {
            "firstname": "Surya",
            "lastname": "K",
            "totalprice": 250,
            "depositpaid": True,
            "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-07"},
            "additionalneeds": "Breakfast",
        }
