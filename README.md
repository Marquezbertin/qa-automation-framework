# 🧪 QA Automation Framework

Este projeto é um framework de testes automatizados que permite testar aplicações Web e APIs, com suporte a relatórios detalhados de execução.

## ✨ Funcionalidades

- Testes de Interface com Selenium WebDriver
- Testes de API com `requests`
- Geração de relatórios com Allure
- Estrutura modular e expansível

## 🚀 Como usar

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/qa-automation-framework.git
cd qa-automation-framework
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute os testes

```bash
python runners/run_ui_tests.py
```

Ou para APIs:

```bash
python runners/run_api_tests.py
```

### 4. Veja os relatórios

Relatórios são gerados na pasta `reports/`.

## 🔧 Tecnologias Usadas

- Python + Selenium
- requests
- pytest
- Allure Reports
