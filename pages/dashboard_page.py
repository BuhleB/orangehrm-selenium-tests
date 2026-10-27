from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    PROFILE_PICTURE = (By.XPATH, "//img[@class='oxd-userdropdown-img']")
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']/parent::a")
    PIM_MENU = (By.XPATH, "//span[text()='PIM']/parent::a")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def is_dashboard_loaded(self):
        return self.is_element_present(self.DASHBOARD_HEADER)
    
    def navigate_to_leave(self):
        self.click(self.LEAVE_MENU)
    
    def navigate_to_pim(self):
        self.click(self.PIM_MENU)
    
    def get_profile_picture_style(self):
        return self.find_element(self.PROFILE_PICTURE).get_attribute("style")