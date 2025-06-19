# 🧪 QA Automation Framework

Este projeto é um framework de testes automatizados que permite testar aplicações Web e APIs, com suporte a geração de relatórios detalhados.

## ✨ Funcionalidades

* ✅ Testes de Interface com Selenium WebDriver
* ✅ Testes de API com `requests`
* ✅ Geração de relatórios com `Allure`
* ✅ Dados de teste dinâmicos com `Faker`
* ✅ Estrutura modular e expansível com `pytest`

## 🚀 Como usar

### 1. Clone o projeto

```bash
git clone https://github.com/Marquezbertin/qa-automation-framework
cd qa-automation-framework
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute os testes

#### Testes de Interface (UI)

```bash
python runners/run_ui_tests.py
```

#### Testes de API

```bash
python runners/run_api_tests.py
```

### 5. Gerar e visualizar relatórios Allure

```bash
allure serve reports/
```

> Os relatórios são gerados automaticamente na pasta `reports/`.

## 🧪 Estrutura do Projeto

```
qa-automation-framework/
├── tests/
│   ├── api/
│   └── ui/
├── runners/
│   ├── run_api_tests.py
│   └── run_ui_tests.py
├── reports/
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔧 Tecnologias Usadas

* Python 3.13+
* Selenium 4.20.0
* requests 2.31.0
* pytest 8.2.0
* allure-pytest 2.13.3
* faker 24.11.0

## 🗃️ .gitignore

Este projeto ignora arquivos de cache e relatórios gerados:

```
__pycache__/
*.pyc
reports/
.env
```
