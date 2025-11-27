from playwright.sync_api import Page


class Footer:
    def __init__(self, page: Page):
        self.page = page

        # Локаторы через XPath
        self.footer = page.locator('//footer[contains(@class, "Footer_root")]')

        # Кнопка "Начать проект"
        self.start_project_button = page.locator(
            '//button[contains(@class, "Footer_button__RHd0Q")]')

        # Конкретные социальные сети по href
        self.behance_button = page.locator(
            '//div[@class="Socials_socialsWrap__DPtp_ Footer_socials__C39yX"]//a[contains(@href, "behance")]'
        )
        self.dprofile_button = page.locator(
            '//div[@class="Socials_socialsWrap__DPtp_ Footer_socials__C39yX"]//a[contains(@href, "dprofile")]'
        )
        self.telegram_button = page.locator(
            '//div[@class="Socials_socialsWrap__DPtp_ Footer_socials__C39yX"]//a[contains(@href, "t.me")]'
        )
        self.vk_button = page.locator(
            '//div[@class="Socials_socialsWrap__DPtp_ Footer_socials__C39yX"]//a[contains(@href, "vk.com")]'
        )

        # Кнопки презентаций
        self.pdf_button = page.locator(
            '//div[@class="Documents_documentsWrap__iNfwU Footer_documents___mRvU"]//a[contains(@href, "pdf")]'
        )
        self.pitch_button = page.locator(
            '//div[@class="Documents_documentsWrap__iNfwU Footer_documents___mRvU"]//a[contains(@href, "pitch")]'
        )