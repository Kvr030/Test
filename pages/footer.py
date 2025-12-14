from playwright.sync_api import Page


class Footer:
    def __init__(self, page: Page):
        self.page = page

        # Футер
        self.footer = page.locator("footer")

        # Кнопка "Начать проект"
        self.start_project_button = page.locator("footer").get_by_role("button", name= "Начать проект")

        # Конкретные социальные сети по href
        self.behance_button = page.locator("footer").get_by_role("link", name="be")
        self.dprofile_button = page.locator("footer").get_by_role("link", name="dp")
        self.telegram_button = page.locator("footer").get_by_role("link", name="tg")
        self.vk_button = page.locator("footer").get_by_role("link", name="vk")

        # Кнопки презентаций
        self.pdf_button = page.locator("footer").get_by_role("link", name="pdf")
        self.pitch_button = page.locator("footer").get_by_role("link", name="pitch")