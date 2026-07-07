"""
Inventory page tests.

Demonstrates: locator filtering, interacting with dynamic lists,
dropdown selection, and assertions on extracted collections.
"""


def test_add_items_updates_cart_badge(standard_user_inventory):
    inventory = standard_user_inventory
    assert inventory.cart_count() == 0

    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.add_item_to_cart("Sauce Labs Bike Light")

    assert inventory.cart_count() == 2


def test_sort_products_low_to_high(standard_user_inventory):
    inventory = standard_user_inventory
    inventory.sort_by("lohi")            # price low -> high

    # Re-read prices and assert they are non-decreasing.
    prices = [
        float(p.replace("$", ""))
        for p in inventory.page.locator(".inventory_item_price").all_inner_texts()
    ]
    assert prices == sorted(prices)


def test_all_products_are_listed(standard_user_inventory):
    # SauceDemo's standard inventory always shows 6 products.
    assert len(standard_user_inventory.product_names()) == 6
