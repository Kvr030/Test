import pytest
import allure
from playwright.sync_api import expect
import time


@allure.feature("Footer Tests")
class TestFooterElements:

    @allure.title("Проверка видимости основного футера")
    def test_footer_visible(self, footer_on_main_page):
        expect(footer_on_main_page.footer).to_be_visible()

    @allure.title("Проверка видимости кнопки 'Начать проект'")
    def test_start_project_button_visible(self, footer_on_main_page):
        expect(footer_on_main_page.start_project_button).to_be_visible()

    @allure.title("Проверка видимости кнопки Behance")
    def test_behance_button_visible(self, footer_on_main_page):
        expect(footer_on_main_page.behance_button).to_be_visible()

    @allure.title("Проверка видимости кнопки DProfile")
    def test_dprofile_button_visible(self, footer_on_main_page):
        expect(footer_on_main_page.dprofile_button).to_be_visible()

    @allure.title("Проверка видимости кнопки Telegram")
    def test_telegram_button_visible(self, footer_on_main_page):
        expect(footer_on_main_page.telegram_button).to_be_visible()

    @allure.title("Проверка видимости кнопки VK")
    def test_vk_button_visible(self, footer_on_main_page):
        expect(footer_on_main_page.vk_button).to_be_visible()

    @allure.title("Проверка видимости кнопки PDF")
    def test_pdf_button_visible(self, footer_on_main_page):
        expect(footer_on_main_page.pdf_button).to_be_visible()

    @allure.title("Проверка видимости кнопки Pitch")
    def test_pitch_button_visible(self, footer_on_main_page):
        expect(footer_on_main_page.pitch_button).to_be_visible()

    # Раскомитить если нужна визуальная проверка
    # @allure.title("Финальная пауза для визуальной проверки")
    # def test_final_visual_check(self, footer_on_main_page):
    #     """Финальный тест с ожиданием для визуальной проверки футера"""
    #     # Подсвечиваем футер для наглядности
    #     footer_on_main_page.page.evaluate("""
    #             document.querySelector('footer').style.border = '3px solid red';
    #         """)
    #
    #     # Ждем 5 секунд для визуальной проверки
    #     time.sleep(10)
    #
    #     # Убираем подсветку
    #     footer_on_main_page.page.evaluate("""
    #             document.querySelector('footer').style.border = '';
    #         """)