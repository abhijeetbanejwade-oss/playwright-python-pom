from playwright.sync_api import Page


class LoginPage:
    """Page Object Model for https://www.saucedemo.com/ login page using Playwright.

    Provides simple, test-friendly methods:
    - open(): navigate to login page
    - login(username, password): perform login
    - get_error_text(): return visible error message text (if any)
    - is_logged_in(): quick check for inventory page
    - clear_fields(): clear username/password inputs
    """

    URL = "https://www.saucedemo.com/"
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test='error']"
    INVENTORY_CONTAINER = "#inventory_container"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator(self.USERNAME)
        self.password = page.locator(self.PASSWORD)
        self.login_btn = page.locator(self.LOGIN_BTN)
        self.error = page.locator(self.ERROR_MSG)

    def open(self):
        """Navigate to the login page."""
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        """Fill credentials and submit the form, then wait for inventory to load."""
        # ensure we're on the login page
        if self.page.url != self.URL:
            self.open()
        # fill fields and click
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()
        # wait for inventory page to be ready so subsequent actions don't race
        try:
            self.page.wait_for_selector(self.INVENTORY_CONTAINER, timeout=10000)
        except Exception:
            # if inventory doesn't appear, test will fail later; swallow to keep behavior
            pass

    def get_error_text(self) -> str:
        """Return the text of the visible error message, or empty string."""
        try:
            if self.error.is_visible():
                return self.error.inner_text().strip()
        except Exception:
            # element may not be attached or visible
            return ""
        return ""

    def is_logged_in(self) -> bool:
        """Quick check for successful login: inventory URL or visible inventory container."""
        try:
            if self.page.url.endswith("/inventory.html"):
                return True
            return self.page.locator(self.INVENTORY_CONTAINER).is_visible()
        except Exception:
            return False

    def clear_fields(self):
        """Clear username and password input fields."""
        try:
            self.username.fill("")
            self.password.fill("")
        except Exception:
            pass
