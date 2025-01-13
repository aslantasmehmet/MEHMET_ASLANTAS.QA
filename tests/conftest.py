import pytest
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            driver.save_screenshot(f'screenshots/failed_test_{timestamp}.png')
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
