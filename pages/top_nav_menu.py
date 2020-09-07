from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TopNavMenu(Page):

    LOGO = (By.ID, 'logo')

    def click_logo(self):
        self.click(*self.LOGO)

    def verify_page(self):
        url = self.driver.current_url
        assert url == 'https://gettop.us/', f'Expected URL - "https://gettop.us/", but got {url}'
