import selenium
import pytest
from selenium import webdriver

def test_page_orange_hrm():
    # Chrome driver setup
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # Wait time ektu bariye din
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Title check
    assert "OrangeHRM" in driver.title
    
    # Browser bondho kora
    driver.quit()