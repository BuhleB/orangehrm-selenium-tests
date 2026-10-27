from selenium.webdriver.common.by import By
from .base_page import BasePage

class LeavePage(BasePage):
    # Locators for Leave module
    APPLY_MENU = (By.XPATH, "//a[text()='Apply']")
    MY_LEAVE_MENU = (By.XPATH, "//a[text()='My Leave']")
    NO_LEAVE_BALANCE_MESSAGE = (By.XPATH, "//div[contains(text(), 'No Leave Types with Leave Balance')]")
    LEAVE_TYPE_DROPDOWN = (By.XPATH, "//div[contains(@class, 'oxd-select-text')]")
    FROM_DATE_FIELD = (By.XPATH, "//label[text()='From Date']/following::input[1]")
    TO_DATE_FIELD = (By.XPATH, "//label[text()='To Date']/following::input[1]")
    COMMENT_FIELD = (By.XPATH, "//textarea")
    APPLY_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'oxd-toast')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(@class, 'oxd-input-field-error-message')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def navigate_to_apply_leave(self):
        """Navigate to Apply Leave section"""
        self.click(self.APPLY_MENU)
    
    def navigate_to_my_leave(self):
        """Navigate to My Leave section"""
        self.click(self.MY_LEAVE_MENU)
    
    def is_no_leave_balance_displayed(self, timeout=None):
        """Check if 'No Leave Types with Leave Balance' message is displayed"""
        return self.is_element_present(self.NO_LEAVE_BALANCE_MESSAGE, timeout)
    
    def attempt_leave_application(self, from_date, to_date, comment=""):
        """
        Attempt to fill out and submit leave application form
        This will fail due to BUG-OHRM-001, but demonstrates form submission
        """
        print("📝 Attempting to fill leave application form...")
        
        # Try to fill form fields (even though it will fail due to the bug)
        if self.is_element_present(self.FROM_DATE_FIELD):
            self.send_keys(self.FROM_DATE_FIELD, from_date)
            print("✅ From date field filled")
        
        if self.is_element_present(self.TO_DATE_FIELD):
            self.send_keys(self.TO_DATE_FIELD, to_date)
            print("✅ To date field filled")
            
        if self.is_element_present(self.COMMENT_FIELD) and comment:
            self.send_keys(self.COMMENT_FIELD, comment)
            print("✅ Comment field filled")
        
        # Try to click apply button if present
        if self.is_element_present(self.APPLY_BUTTON):
            self.click(self.APPLY_BUTTON)
            print("✅ Apply button clicked")
            return True
        else:
            print("❌ Apply button not available (due to bug)")
            return False
    
    def is_success_message_displayed(self):
        """Check if leave application was successful"""
        return self.is_element_present(self.SUCCESS_MESSAGE)
    
    def get_error_message(self):
        """Get any error message displayed"""
        if self.is_element_present(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
    
    def is_leave_type_dropdown_available(self):
        """Check if leave type dropdown is available for selection"""
        return self.is_element_present(self.LEAVE_TYPE_DROPDOWN)