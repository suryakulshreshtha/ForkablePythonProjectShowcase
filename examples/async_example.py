"""
Standalone example of the Playwright ASYNC API.

Why is this a script and not a pytest test?
  `pytest-playwright`'s fixtures (page/context/browser) are SYNC. Mixing
  them with pytest-asyncio causes event-loop conflicts. The whole test
  suite therefore uses the sync API (the pytest-playwright default), and
  this file shows the async API on its own so the framework demonstrates
  both styles cleanly.

Run it directly:
    python examples/async_example.py
"""
import asyncio
import re

from playwright.async_api import async_playwright, expect

UI_BASE_URL = "https://www.saucedemo.com"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()       # isolated, incognito-like
        page = await context.new_page()

        await page.goto(UI_BASE_URL)
        await expect(page).to_have_title("Swag Labs")

        await page.get_by_placeholder("Username").fill("standard_user")
        await page.get_by_placeholder("Password").fill("secret_sauce")
        await page.get_by_role("button", name="Login").click()

        await expect(page).to_have_url(re.compile(r"inventory"))
        print("Async login flow passed ✅")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
