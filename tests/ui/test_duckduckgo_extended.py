from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Testa se sugestões de autocompletar aparecem
def test_autocomplete_suggestions(driver):
    driver.get("https://duckduckgo.com")
    search_box = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("automation")

    # Novo seletor de sugestões com fallback
    suggestions_box = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".search__autocomplete li span"))
    )

    assert len(suggestions_box) > 0, "❌ Nenhuma sugestão de autocompletar encontrada."
    print("✅ Sugestões de autocompletar carregadas com sucesso.")


# 2. Testa clique no primeiro resultado
def test_click_first_search_result(driver):
    driver.get("https://duckduckgo.com")
    search_box = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Python programming")
    search_box.submit()

    result_links = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
    )

    assert result_links, "❌ Nenhum resultado encontrado."
    result_links[0].click()

    WebDriverWait(driver, 15).until(lambda d: "duckduckgo.com" not in d.current_url)
    print("✅ Primeiro resultado acessado com sucesso.")


# 3. Busca em branco
def test_blank_search(driver):
    driver.get("https://duckduckgo.com")
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.submit()

    assert "duckduckgo.com" in driver.current_url
    print("✅ Busca vazia não redirecionou indevidamente.")


# 4. Caracteres especiais com termo funcional
def test_special_characters_search(driver):
    driver.get("https://duckduckgo.com")
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("[QA] #automated-tests!")
    search_box.submit()

    results = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
    )

    assert results, "❌ Nenhum resultado retornado para caracteres especiais."
    print("✅ Resultados retornados com sucesso usando caracteres especiais.")


# 5. Verifica botão de busca
def test_search_button_present(driver):
    driver.get("https://duckduckgo.com")
    # Novo seletor: botão pode estar dentro de um form
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit'][id^='search_button']"))
    )

    assert button.is_enabled()
    print("✅ Botão de busca está visível e habilitado.")


# 6. Teste extra: valida título da página
def test_title_contains_duckduckgo(driver):
    driver.get("https://duckduckgo.com")
    WebDriverWait(driver, 10).until(lambda d: "DuckDuckGo" in d.title)
    print("✅ Título da página validado.")
