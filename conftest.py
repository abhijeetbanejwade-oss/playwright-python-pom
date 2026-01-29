import os
import pytest
from playwright.sync_api import sync_playwright
from Pages.login_page import LoginPage
from Pages.sanity_check import PagesSanityCheck


# Use environment variable PLAYWRIGHT_HEADLESS to control headless mode (default: True)
HEADLESS = os.getenv("PLAYWRIGHT_HEADLESS", "true").lower() in ("true", "1", "yes")


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def login_page(page):
    """Return a LoginPage instance with the page already navigated to the login URL."""
    lp = LoginPage(page)
    lp.open()
    return lp


@pytest.fixture
def pages_sanity_check(page):
    """Return a PagesSanityCheck instance for inventory/cart flows."""
    return PagesSanityCheck(page)
