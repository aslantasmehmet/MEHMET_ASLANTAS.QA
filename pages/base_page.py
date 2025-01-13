from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, test_name):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        screenshot_path = os.path.join(screenshot_dir, f'{test_name}_{timestamp}.png')
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path
