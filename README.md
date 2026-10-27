# OrangeHRM Selenium Tests (pytest)

UI test automation for the public [OrangeHRM demo](https://opensource-demo.orangehrmlive.com/), written in Python with Selenium and pytest using the Page Object Model.

Created during the CAPACITI software testing programme.

## What it covers

| Test | Checks |
| --- | --- |
| `test_successful_login` | Valid credentials reach the dashboard |
| `test_login_with_invalid_credentials_is_rejected` | Wrong password and wrong username both show "Invalid credentials" and never reach the dashboard |
| `test_forgot_password_link_opens_reset_page` | The "Forgot your password?" link is present and opens the password reset page |
| `test_username_is_not_case_sensitive` | Observation (BUG-OHRM-007): logging in as `admin` works. Marked `observation` because it may be intended behaviour |
| `test_apply_leave_form_is_available` | Known issue (BUG-OHRM-001): Apply Leave can show "No Leave Types with Leave Balance". Marked `xfail` because it depends on the demo data |

## Design

- **Page Object Model:** `LoginPage`, `DashboardPage`, `LeavePage` on a shared `BasePage`.
- **Fixtures (`conftest.py`):** a Chrome driver per test, page-object fixtures and a `logged_in` fixture, so tests contain no setup or teardown code.
- **Explicit waits only:** no `time.sleep`. Checks that something is *not* there use a short timeout.
- **Real assertions:** a defect shows up as a failing assertion with a clear message, not a deliberate `pytest.fail()`.
- **Known issues:** `xfail(strict=False)` records a known defect and reports XPASS once it is fixed.
- **Reporting:** an HTML report with a screenshot attached to every failed test.

## Getting started

Requires Python 3.9+ and Google Chrome.

```bash
pip install -r requirements.txt
pytest                      # runs all tests, report in reports/report.html
HEADLESS=1 pytest           # run without opening a browser window
pytest -m "not observation" # skip the observation test
```

Failure screenshots are also saved to `reports/screenshots/`.

## Test data

The tests use the demo site's publicly documented credentials (`Admin` / `admin123`). No private data is involved.
