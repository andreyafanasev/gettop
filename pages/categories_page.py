from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Categories(Page):

    ALL_CATEG = (By.CSS_SELECTOR, 'div.product-category')
    CAT_ACCESS = (By.CSS_SELECTOR, "a[href='https://gettop.us/product-category/accessories/']")
    CAT_IPAD = (By.CSS_SELECTOR, "div.col-inner a[href='https://gettop.us/product-category/ipad/']")
    CAT_IPHONE = (By.CSS_SELECTOR, "div.col-inner a[href='https://gettop.us/product-category/iphone/']")
    CAT_MAC = (By.CSS_SELECTOR, "div.col-inner a[href='https://gettop.us/product-category/macbook/']")
    HEADER = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb')

    def verify_categ_shown(self):
        NEEDED_CAT = ['ACCESSORIES', 'IPAD', 'IPHONE', 'MACBOOK']
        e = self.find_elements(*self.ALL_CATEG)
        for i in range(len(e)):
            assert NEEDED_CAT[i] in e[i].text, f'Expected category {NEEDED_CAT[i]}, but got {e[i].text}'

    def click_access_cat(self):
        self.click(*self.CAT_ACCESS)

    def click_ipad_cat(self):
        self.click(*self.CAT_IPAD)

    def click_iphone_cat(self):
        self.click(*self.CAT_IPHONE)

    def click_mac_cat(self):
        self.click(*self.CAT_MAC)

    def verify_access_cat(self):
        self.assert_text('ACCESSORIES', *self.HEADER)

    def verify_ipad_cat(self):
        self.assert_text('IPAD', *self.HEADER)

    def verify_iphone_cat(self):
        self.assert_text('IPHONE', *self.HEADER)

    def verify_mac_cat(self):
        self.assert_text('MACBOOK', *self.HEADER)
