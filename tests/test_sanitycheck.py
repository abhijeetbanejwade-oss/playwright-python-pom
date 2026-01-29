def test_e2e_flow(login_page, pages_sanity_check):
    # Login
    login_page.login("standard_user", "secret_sauce")

    # Add items to cart
    pages_sanity_check.add_item_to_cart()

    # Go to cart
    pages_sanity_check.go_to_cart()

    # Proceed to checkout
    pages_sanity_check.proceed_to_checkout()
    pages_sanity_check.fill_checkout_info()
    pages_sanity_check.continue_checkout()
    pages_sanity_check.finish_checkout()
