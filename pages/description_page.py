from pages.base_page import Page
from selenium.webdriver.common.by import By


class Description(Page):

    DESCR = (By.ID, 'tab-description')

    def verify_description(self):
        self.find_element(*self.DESCR)