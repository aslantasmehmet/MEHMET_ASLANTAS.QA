from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time

class QAJobsPage(BasePage):
    # URLs
    QA_CAREERS_URL = "https://useinsider.com/careers/quality-assurance/"
    
    # Locators
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
    
    # Filter locators
    LOCATION_FILTER = (By.ID, "filter-by-location")
    DEPARTMENT_FILTER = (By.ID, "filter-by-department")
    
    # Job listings
    JOB_LIST = (By.CSS_SELECTOR, "div.position-list-item-wrapper")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)

    def navigate_to_qa_careers(self):
        """Navigate directly to QA Careers page"""
        self.driver.get(self.QA_CAREERS_URL)
        time.sleep(10)  # Wait for page load
        
        # Scroll down the page slowly to load all elements
        for i in range(10):
            self.driver.execute_script(f"window.scrollTo(0, {i * 500});")
            time.sleep(0.5)
        
        # Scroll back to top
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def click_see_all_qa_jobs(self):
        """Click on 'See all QA jobs' button"""
        try:
            # Wait for button to be clickable
            button = self.wait.until(
                EC.element_to_be_clickable(self.SEE_ALL_QA_JOBS_BUTTON)
            )
            
            # Print button details for debugging
            print(f"Button text: {button.text}")
            print(f"Button href: {button.get_attribute('href')}")
            
            # Scroll to button
            self.driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - 100);", button)
            time.sleep(3)
            
            # Click the button
            button.click()
            time.sleep(7)  # Wait for new page to load
            return True
            
        except Exception as e:
            print("Failed to click 'See all QA jobs' button:", str(e))
            self.take_screenshot("see_all_qa_jobs_failed")
            return False

    def apply_filters(self):
        """Apply both location and department filters"""
        try:
            # Wait for filters to be present
            location_filter = self.wait.until(
                EC.presence_of_element_located(self.LOCATION_FILTER)
            )
            department_filter = self.wait.until(
                EC.presence_of_element_located(self.DEPARTMENT_FILTER)
            )
            
            # Create Select objects
            location_select = Select(location_filter)
            department_select = Select(department_filter)
            
            # Scroll to filters
            self.driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - 100);", location_filter)
            time.sleep(2)
            
            # Select Istanbul location
            print("Selecting Istanbul location...")
            for option in location_select.options:
                if "Istanbul, Turkey" in option.text:
                    location_select.select_by_visible_text(option.text)
                    break
            time.sleep(3)
            
            # Select Quality Assurance department
            print("Selecting Quality Assurance department...")
            for option in department_select.options:
                if "Quality Assurance" in option.text:
                    department_select.select_by_visible_text(option.text)
                    break
            time.sleep(3)
            
            return True
            
        except Exception as e:
            print("Failed to apply filters:", str(e))
            self.take_screenshot("apply_filters_failed")
            return False

    def are_job_positions_available(self):
        """Check if there are any job positions listed"""
        try:
            jobs = self.wait.until(
                EC.presence_of_all_elements_located(self.JOB_LIST)
            )
            jobs_count = len(jobs)
            print(f"Found {jobs_count} job positions in Istanbul for Quality Assurance")
            return jobs_count > 0
        except Exception as e:
            print("Failed to check job positions:", str(e))
            self.take_screenshot("check_jobs_failed")
            return False
