import pytest


def test_successful_login(login_page, dashboard_page, config):
    login_page.navigate_to_login()
    login_page.login(config.USERNAME, config.PASSWORD)

    assert dashboard_page.is_dashboard_loaded(), "Dashboard did not load after valid login"


@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "wrongpassword"),
        ("wronguser", "admin123"),
    ],
    ids=["wrong_password", "wrong_username"],
)
def test_login_with_invalid_credentials_is_rejected(login_page, driver, username, password):
    login_page.navigate_to_login()
    login_page.login(username, password)

    assert login_page.is_invalid_credentials_error_displayed(), "No 'Invalid credentials' message shown"
    assert "dashboard" not in driver.current_url, "User reached the dashboard with invalid credentials"


@pytest.mark.observation
def test_username_is_not_case_sensitive(login_page, dashboard_page, config):
    """BUG-OHRM-007 (observation). Logging in as 'admin' instead of 'Admin' succeeds.

    This test passes while that behaviour exists. Many systems treat usernames as
    case-insensitive on purpose, so whether this is a defect is a product decision.
    """
    login_page.navigate_to_login()
    login_page.login(config.USERNAME.lower(), config.PASSWORD)

    assert dashboard_page.is_dashboard_loaded()


def test_forgot_password_link_opens_reset_page(login_page, driver):
    login_page.navigate_to_login()

    assert login_page.is_forgot_password_link_displayed(), "Forgot password link not found on login page"
    login_page.click_forgot_password()

    assert "passwordreset" in driver.current_url.lower(), f"Unexpected page after click: {driver.current_url}"
