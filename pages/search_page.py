from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Search(Page):

    SEARCH_ICON = (By.CSS_SELECTOR, 'li.header-search')
    INPUT_FIELD = (By.ID, 'woocommerce-product-search-field-0')
    SUBMIT_SEARCH = (By.XPATH, '//button[@value="Search"]')
    SEARCH_ITEM = (By.CSS_SELECTOR, 'nav.breadcrumbs')
    NO_ITEM_TXT = (By.CSS_SELECTOR, 'div.shop-container')

    def hover_over_search(self):
        search_icon = self.driver.find_element(*self.SEARCH_ICON)
        self.actions.move_to_element(search_icon).perform()

    def search_for(self, search_item):
        self.input(search_item, *self.INPUT_FIELD)
        sleep(2)

    def submit_search(self):
        self.click(*self.SUBMIT_SEARCH)

    def verify_search_page(self, search_item):
        self.assert_text(search_item, *self.SEARCH_ITEM)

    def verify_search_wrong(self):
        self.assert_text('No products were found matching your selection', *self.NO_ITEM_TXT)
