from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Quality Assurance")
    search_box.submit()
    assert "Quality Assurance" in driver.title
    driver.quit()
