import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")   # একবারই ব্রাউজার খুলবে পুরো module-এর জন্য
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_yt_search(driver):
    driver.get("https://www.youtube.com/")
    search = driver.find_element(By.NAME, "search_query")
    search.send_keys("selenium playlist")
    search.submit()
    WebDriverWait(driver, 9).until(EC.title_contains("selenium playlist"))
    assert "selenium playlist" in driver.title.lower()




# python -m pytest test_youtube.py
