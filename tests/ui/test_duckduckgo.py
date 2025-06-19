from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_duckduckgo_search(driver):
    print("🔎 Acessando DuckDuckGo...")
    driver.get("https://www.duckduckgo.com")

    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys("Quality Assurance")
    search_box.submit()

    print("📄 Título após busca:", driver.title)

    WebDriverWait(driver, 10).until(
        lambda d: "quality assurance" in d.title.lower()
    )

    assert "quality assurance" in driver.title.lower()
