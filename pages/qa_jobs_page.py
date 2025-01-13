from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
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
    VIEW_ROLE_BUTTON = (By.XPATH, "//a[contains(text(), 'View Role')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(self.driver)

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

    def hover_and_click_view_role(self):
        """Hover over a job listing and click the View Role button"""
        try:
            # Wait for job listings and get the first one
            job_listings = self.wait.until(
                EC.presence_of_all_elements_located(self.JOB_LIST)
            )
            
            if not job_listings:
                print("No job listings found")
                return False
            
            # Get the first job listing
            job = job_listings[0]
            
            # Scroll the job into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", job)
            time.sleep(2)
            
            # Hover over the job listing
            print("Hovering over job listing...")
            self.actions.move_to_element(job).perform()
            time.sleep(2)
            
            try:
                # Try to find the View Role button within this specific job listing
                view_role_button = job.find_element(By.XPATH, ".//a[contains(text(), 'View Role')]")
                print("Found View Role button")
            except Exception as e:
                print("Could not find View Role button in the first job listing, trying next one...")
                # If not found in first job, try the second one
                if len(job_listings) > 1:
                    job = job_listings[1]
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", job)
                    time.sleep(2)
                    self.actions.move_to_element(job).perform()
                    time.sleep(2)
                    view_role_button = job.find_element(By.XPATH, ".//a[contains(text(), 'View Role')]")
                else:
                    raise Exception("No View Role button found in any job listing")
            
            # Store the current window handle
            current_window = self.driver.current_window_handle
            
            # Click the button
            print("Clicking View Role button...")
            view_role_button.click()
            time.sleep(5)
            
            # Switch to the new window
            print("Available window handles:", self.driver.window_handles)
            for window_handle in self.driver.window_handles:
                if window_handle != current_window:
                    self.driver.switch_to.window(window_handle)
                    break
            
            # Check if we're on the Lever application page
            current_url = self.driver.current_url
            print(f"Current URL: {current_url}")
            
            if "jobs.lever.co" in current_url or "lever.co" in current_url:
                print("Successfully redirected to Lever application page")
                return True
            else:
                print("Not on Lever application page")
                return False
            
        except Exception as e:
            print("Failed to hover and click View Role:", str(e))
            self.take_screenshot("view_role_failed")
            return False

    def verify_job_listings(self):
        """Verify that all job listings match the selected filters"""
        try:
            # Wait for job listings to be present and scroll to them
            job_listings = self.wait.until(
                EC.presence_of_all_elements_located(self.JOB_LIST)
            )
            
            if not job_listings:
                print("No job listings found")
                return False
                
            print(f"Found {len(job_listings)} job listings")
            
            # Check each job listing
            for job in job_listings:
                try:
                    # Get the full text of the job listing
                    job_text = job.text
                    print(f"\nJob listing text: {job_text}")
                    
                    # Check if the required texts are in the job listing
                    if "Istanbul, Turkey" not in job_text:
                        print("Job listing does not contain 'Istanbul, Turkey'")
                        return False
                        
                    if "Quality Assurance" not in job_text:
                        print("Job listing does not contain 'Quality Assurance'")
                        return False
                        
                except Exception as e:
                    print(f"Failed to check job listing: {str(e)}")
                    return False
            
            print("\nAll job listings match the filter criteria!")
            return True
            
        except Exception as e:
            print("Failed to verify job listings:", str(e))
            self.take_screenshot("verify_jobs_failed")
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
