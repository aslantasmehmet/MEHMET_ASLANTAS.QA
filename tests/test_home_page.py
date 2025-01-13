import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage

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
