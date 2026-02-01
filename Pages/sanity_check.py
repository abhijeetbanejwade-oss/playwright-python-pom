from playwright.sync_api import Page


class PagesSanityCheck:
    add_to_cart_button = "#add-to-cart-sauce-labs-backpack"
    cart_badge = ".shopping_cart_badge"
    cart_icon = ".shopping_cart_link"
    checkout_button = "#checkout"
    first_name_input = "#first-name"
    last_name_input = "#last-name"
    postal_code_input = "#postal-code"
    continue_button = "#continue"
    finish_button = "#finish"
    order_complete_header = ".complete-header"

    def __init__(self, page: Page):
        self.page = page

    def add_item_to_cart(self):
        # wait for the button and click once
        self.page.wait_for_selector(self.add_to_cart_button, timeout=10000)
        self.page.locator(self.add_to_cart_button).click()
        # wait for cart badge to indicate item added
        try:
            self.page.wait_for_selector(self.cart_badge, timeout=5000)
        except Exception:
            pass

    def go_to_cart(self):
        self.page.locator(self.cart_icon).click()

    def proceed_to_checkout(self):
        self.page.locator(self.checkout_button).click()

    def fill_checkout_info(self):
        self.page.locator(self.first_name_input).fill("John")
        self.page.locator(self.last_name_input).fill("Doe")
        self.page.locator(self.postal_code_input).fill("12345")

    def continue_checkout(self):
        self.page.locator(self.continue_button).click()

    def finish_checkout(self):
        self.page.locator(self.finish_button).click()

    def is_order_complete(self) -> bool:
        try:
            return self.page.locator(self.order_complete_header).is_visible()
        except Exception:
            return False


