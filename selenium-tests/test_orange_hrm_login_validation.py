import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_page_orange_hrm():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # ৩. টাইটেল চেক করা
    assert "OrangeHRM" in driver.title
    
    driver.find_element(By.NAME, "username").send_keys("Admin")
   
    driver.find_element(By.NAME, "password").send_keys("admin123")
    
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    time.sleep(3)
    
    assert "dashboard" in driver.current_url

    driver.quit()
    # python -m pytest -v test_orange_hrm_login_validation.py