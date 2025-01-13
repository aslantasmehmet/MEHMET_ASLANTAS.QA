from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    LOGO = (By.CSS_SELECTOR, "a.navbar-brand")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/"

    def navigate_to(self):
        self.driver.get(self.url)

    def is_page_loaded(self):
        return self.is_element_visible(self.LOGO)
