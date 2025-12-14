import allure
import pytest
from playwright.sync_api import expect

@allure.feature("Footer Tests")
class TestFooterElements:

    @allure.title("Проверка видимости основного футера")
    def test_footer_visible(self, footer):
        expect(footer.footer).to_be_visible()

    @allure.title("Проверка видимости кнопки 'Начать проект'")
    def test_start_project_button_visible(self, footer):
        expect(footer.start_project_button).to_be_visible()

    @allure.title("Проверка видимости кнопки Behance")
    def test_behance_button_visible(self, footer):
        expect(footer.behance_button).to_be_visible()

    @allure.title("Проверка видимости кнопки DProfile")
    def test_dprofile_button_visible(self, footer):
        expect(footer.dprofile_button).to_be_visible()

    @allure.title("Проверка видимости кнопки Telegram")
    def test_telegram_button_visible(self, footer):
        expect(footer.telegram_button).to_be_visible()

    @allure.title("Проверка видимости кнопки VK")
    def test_vk_button_visible(self, footer):
        expect(footer.vk_button).to_be_visible()

    @allure.title("Проверка видимости кнопки PDF")
    def test_pdf_button_visible(self, footer):
        expect(footer.pdf_button).to_be_visible()

    @allure.title("Проверка видимости кнопки Pitch")
    def test_pitch_button_visible(self, footer):
        expect(footer.pitch_button).to_be_visible()