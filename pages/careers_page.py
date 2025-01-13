from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class CareersPage(BasePage):
    # Locators for navigation
    COMPANY_MENU = (By.XPATH, "//a[contains(text(),'Company')]")
    CAREERS_LINK = (By.CSS_SELECTOR, "a[href*='careers']")
    
    # Block elements to verify
    LOCATIONS_BLOCK = (By.CSS_SELECTOR, "section#career-our-location")
    TEAMS_BLOCK = (By.CSS_SELECTOR, "section#career-find-our-calling")
    LIFE_INSIDER_BLOCK = (By.XPATH, "//h2[contains(@class, 'elementor-heading-title') and contains(text(), 'Life at Insider')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)

    def click_company_menu(self):
        try:
            # Wait for page load and click Company menu
            company_menu = self.wait.until(
                EC.element_to_be_clickable(self.COMPANY_MENU)
            )
            company_menu.click()
            time.sleep(1)  # Wait for dropdown to appear
            return True
        except Exception as e:
            self.take_screenshot("company_menu_click_failed")
            print("Failed to click Company menu:", str(e))
            return False

    def click_careers(self):
        try:
            # Find and click Careers link in dropdown
            careers_link = self.wait.until(
                EC.element_to_be_clickable(self.CAREERS_LINK)
            )
            careers_link.click()
            time.sleep(7)  # Wait longer for page load and animations
            return True
        except Exception as e:
            self.take_screenshot("careers_click_failed")
            print("Failed to click Careers link:", str(e))
            return False

    def scroll_to_element(self, element):
        """Scroll element into view using JavaScript"""
        try:
            # First scroll near the element
            self.driver.execute_script("""
                var viewPortHeight = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
                var elementTop = arguments[0].getBoundingClientRect().top;
                window.scrollBy(0, elementTop - (viewPortHeight / 2));
            """, element)
            time.sleep(2)
            
            # Then ensure it's in view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
            time.sleep(1)
        except Exception as e:
            print(f"Failed to scroll to element: {str(e)}")

    def is_block_visible(self, locator, block_name):
        try:
            print(f"Checking visibility of {block_name}...")
            
            # Find the element
            block = self.wait.until(
                EC.presence_of_element_located(locator)
            )
            
            # Print element details for debugging
            location = block.location
            size = block.size
            class_name = block.get_attribute("class")
            tag_name = block.tag_name
            text = block.text
            print(f"{block_name} - location: {location}, size: {size}")
            print(f"{block_name} - tag: {tag_name}, class: {class_name}, text: {text}")
            
            # Scroll to the element
            self.scroll_to_element(block)
            
            # Check if it's visible
            is_visible = block.is_displayed()
            print(f"{block_name} is_displayed: {is_visible}")
            
            return is_visible
            
        except Exception as e:
            print(f"{block_name} block is not visible:", str(e))
            return False

    def verify_all_blocks_visible(self):
        try:
            # Wait for initial page load
            time.sleep(5)
            
            # Scroll to top first
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            
            # Check each block with proper scrolling
            blocks_status = {
                "Locations": self.is_block_visible(self.LOCATIONS_BLOCK, "Locations"),
                "Teams": self.is_block_visible(self.TEAMS_BLOCK, "Teams"),
                "Life at Insider": self.is_block_visible(self.LIFE_INSIDER_BLOCK, "Life at Insider")
            }
            
            # Report any invisible blocks
            invisible_blocks = [name for name, status in blocks_status.items() if not status]
            
            if invisible_blocks:
                print(f"Following blocks are not visible: {', '.join(invisible_blocks)}")
                self.take_screenshot("invisible_blocks")
                return False
                
            return True
            
        except Exception as e:
            self.take_screenshot("verify_blocks_failed")
            print("Failed to verify blocks:", str(e))
            return False
