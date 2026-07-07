"""
Central configuration.

Values are read from environment variables first (so CI / different
environments can override them) and fall back to public demo sites that
are safe and stable to automate against.
"""
import os

# UI application under test — Sauce Labs' public demo store.
UI_BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")

# REST API under test — restful-booker, a free public practice API.
API_BASE_URL = os.getenv("API_BASE_URL", "https://restful-booker.herokuapp.com")

# Default timeout (ms) for expect() assertions and actions.
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
