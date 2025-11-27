import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def browser():
    """Фикстура запускает браузер и создает страницу"""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture(scope="session")
def footer_on_main_page(browser: Page):
    """Фикстура создает Footer и подготавливает страницу"""
    from pages.footer import Footer
    footer = Footer(browser)
    footer.page.goto("https://only.digital/")
    footer.footer.scroll_into_view_if_needed()

    return footer