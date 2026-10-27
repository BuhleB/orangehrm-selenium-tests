import pytest


@pytest.mark.xfail(
    reason="BUG-OHRM-001: demo admin can have no leave balance, so Apply Leave shows "
           "'No Leave Types with Leave Balance'. Depends on the demo data; XPASS means it is fixed.",
    strict=False,
)
def test_apply_leave_form_is_available(logged_in, dashboard_page, leave_page, config):
    dashboard_page.navigate_to_leave()
    leave_page.navigate_to_apply_leave()

    assert not leave_page.is_no_leave_balance_displayed(timeout=config.SHORT_WAIT), (
        "Apply Leave shows 'No Leave Types with Leave Balance'"
    )
    assert leave_page.is_leave_type_dropdown_available(), "Leave type dropdown not available"
