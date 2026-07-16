import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()

def test_google_navigate(driver):
    driver.get("https://www.google.com/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("what is selenium?")
    time.sleep(3)
    assert "Google" in driver.title


#python -m pytest test_google_search.py -v