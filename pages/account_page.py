from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Account(Page):

    ACCOUNT_ICON = (By.CSS_SELECTOR, 'i.icon-user')
    LOGIN_PAGE = (By.CSS_SELECTOR, 'div.account-container')

    def click_account(self):
        self.click(*self.ACCOUNT_ICON)

    def verify_login_form_open(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.LOGIN_PAGE))