# Only.Digital Footer Tests

Автотесты для проверки элементов футера на сайте [only.digital](https://only.digital/)

## Технологии

- Python
- Pytest
- Playwright
- Allure Reports

## Установка


# Установка зависимостей
pip install playwright pytest allure-pytest pytest-playwright

# Установка браузеров Playwright
playwright install

## Запуск тестов


# Все тесты
pytest

# С генерацией Allure отчетов
pytest --alluredir=allure-results
allure serve allure-results

# Конкретный тест
pytest tests/test_footer.py::TestFooterElements::test_footer_visible -v

onlydigital-footer-test/
├── pages/           # Page Object модели
├── tests/           # Тесты
├── conftest.py      # Фикстуры Pytest
├── requirements.txt # Зависимости
└── pytest.ini      # Конфигурация Pytest

Тесты проверяют
✅ Наличие основного футера

✅ Кнопку "Начать проект"

✅ Кнопки социальных сетей (Behance, DProfile, Telegram, VK)

✅ Кнопки презентаций (PDF, Pitch)