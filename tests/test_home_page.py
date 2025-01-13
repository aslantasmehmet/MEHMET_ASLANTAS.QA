import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage

@pytest.fixture
def driver():
    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_home_page_loaded(driver):
    try:
        # Initialize home page
        home_page = HomePage(driver)
        
        # Navigate to the homepage
        home_page.navigate_to()
        
        # Check if the page is loaded successfully
        assert home_page.is_page_loaded(), "Home page is not loaded properly"
        
    except Exception as e:
        # Take screenshot if test fails
        home_page.take_screenshot("test_home_page_loaded")
        raise e

def test_careers_page_sections(driver):
    try:
        # Initialize pages
        home_page = HomePage(driver)
        careers_page = CareersPage(driver)

        # Navigate to homepage
        home_page.navigate_to()

        # Navigate to Careers page
        careers_page.click_company_menu()
        careers_page.click_careers()

        # Verify all sections are visible
        assert careers_page.verify_all_blocks_visible(), "Not all career page sections are visible"

    except Exception as e:
        # Take screenshot if test fails
        careers_page.take_screenshot("test_careers_page_sections")
        raise e

def test_qa_jobs_istanbul(driver):
    try:
        # Initialize QA jobs page
        qa_jobs_page = QAJobsPage(driver)

        # Navigate to QA careers page
        qa_jobs_page.navigate_to_qa_careers()

        # Click See all QA jobs button
        assert qa_jobs_page.click_see_all_qa_jobs(), "Failed to click 'See all QA jobs' button"

        # Apply location and department filters
        assert qa_jobs_page.apply_filters(), "Failed to apply filters"

        # Verify jobs are available
        assert qa_jobs_page.are_job_positions_available(), "No job positions found in Istanbul for Quality Assurance"

    except Exception as e:
        # Take screenshot if test fails
        qa_jobs_page.take_screenshot("test_qa_jobs_istanbul")
        raise e
