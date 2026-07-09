import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_page_orange_hrm():
    # Chrome driver automatic setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Title check
    assert "OrangeHRM" in driver.title
    
    # Browser bondho kora
    driver.quit()

    #  python -m pytest -v test_orange_hrm_login_validation.py