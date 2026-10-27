import os
from datetime import datetime

import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage
from pages.login_page import LoginPage
from utilities.config import Config


@pytest.fixture
def driver():
    """One Chrome session per test. Set HEADLESS=1 to run without a window."""
    options = Options()
    options.add_argument("--window-size=1920,1080")
    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)  # Selenium Manager resolves the driver
    yield browser
    browser.quit()


@pytest.fixture
def config():
    return Config


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver)


@pytest.fixture
def leave_page(driver):
    return LeavePage(driver)


@pytest.fixture
def logged_in(login_page, dashboard_page, config):
    """Logs in as the demo admin and waits for the dashboard."""
    login_page.navigate_to_login()
    login_page.login(config.USERNAME, config.PASSWORD)
    assert dashboard_page.is_dashboard_loaded(), "Setup failed: could not log in"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """On failure, save a screenshot and attach it to the HTML report."""
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    driver = item.funcargs.get("driver")
    if driver is None:
        return
    try:
        os.makedirs("reports/screenshots", exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = f"{item.name}_{stamp}.png".replace("[", "_").replace("]", "")
        driver.save_screenshot(os.path.join("reports", "screenshots", name))
        report.extras = getattr(report, "extras", []) + [extras.png(driver.get_screenshot_as_base64())]
    except Exception:
        pass  # a failed screenshot must never hide the real test failure
