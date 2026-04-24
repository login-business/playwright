def test_add_to_cart(logged_in_page):

    logged_in_page.verify_inventory_page()
    logged_in_page.add_first_item_to_cart()
    logged_in_page.verify_cart_count(1)