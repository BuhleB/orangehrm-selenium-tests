from selenium.webdriver.common.by import By

from utilities.config import Config
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    # Text-based and tag-agnostic, so it does not depend on OrangeHRM's CSS class names
    FORGOT_PASSWORD_LINK = (By.XPATH, "//*[contains(normalize-space(text()), 'Forgot your password')]")
    INVALID_CREDENTIALS_ALERT = (By.XPATH, "//p[normalize-space()='Invalid credentials']")

    def navigate_to_login(self):
        self.driver.get(Config.BASE_URL)

    def login(self, username, password):
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def is_forgot_password_link_displayed(self):
        return self.is_element_present(self.FORGOT_PASSWORD_LINK)

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    def is_invalid_credentials_error_displayed(self):
        return self.is_element_present(self.INVALID_CREDENTIALS_ALERT)
