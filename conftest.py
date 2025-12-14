import pytest
from playwright.sync_api import sync_playwright
from pages.footer import Footer


@pytest.fixture(scope="session")
def only_digital_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://only.digital/")
        yield page
        browser.close()


@pytest.fixture(scope="session")
def footer(only_digital_page):
    return Footer(only_digital_page)

# @pytest.fixture
# def only_digital_page(page):
#     page.goto("https://only.digital/")
#     return page
#
# @pytest.fixture
# def footer(only_digital_page):
#     return Footer(only_digital_page)