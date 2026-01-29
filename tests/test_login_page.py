from Pages.login_page import LoginPage


# Test credentials from saucedemo
VALID_USER = ("standard_user", "secret_sauce")
LOCKED_OUT_USER = ("locked_out_user", "secret_sauce")
INVALID_USER = ("invalid_user", "bad_pass")


def test_valid_login(login_page):
    username, password = VALID_USER
    login_page.login(username, password)
    assert login_page.is_logged_in(), "Expected to be on inventory page after valid login"


def test_locked_out_user_shows_error(login_page):
    username, password = LOCKED_OUT_USER
    login_page.login(username, password)
    err = login_page.get_error_text()
    assert err and "locked out" in err.lower(), f"Expected locked out error, got: {err}"


def test_invalid_credentials_shows_error(login_page):
    username, password = INVALID_USER
    login_page.login(username, password)
    err = login_page.get_error_text()
    assert err and ("do not match" in err.lower() or "username and password" in err.lower()), f"Expected invalid credentials error, got: {err}"


def test_empty_fields_shows_error(login_page):
    # attempt login with empty username and password
    login_page.login("", "")
    err = login_page.get_error_text()
    # the site may show different messages; check for common keywords
    assert err and ("username is required" in err.lower() or "required" in err.lower()), f"Expected required field error, got: {err}"
