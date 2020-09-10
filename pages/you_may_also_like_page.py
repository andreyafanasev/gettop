from pages.base_page import Page
from selenium.webdriver.common.by import By


class YouMayAlsoLike(Page):

    YOU_MAY = (By.CSS_SELECTOR, '#product-sidebar h3')
    PROD_TITLES = (By.CSS_SELECTOR, '#product-sidebar .product-title')
    MAC_16 = (By.CSS_SELECTOR, ".widget-upsell a[title='MacBook Pro 16-inch']")
    MAC_13 = (By.CSS_SELECTOR, ".widget-upsell a[title='MacBook Pro 13-inch']")
    PROD_TITLE = (By.CSS_SELECTOR, 'h1.product_title')


    def verify_may_like_shown(self):
        self.assert_text('You may also like…', *self.YOU_MAY)

    def verify_you_may_prod_title(self):
        self.find_elements(*self.PROD_TITLES)

    def click_mac_pro_16(self):
        self.click(*self.MAC_16)

    def click_mac_pro_13(self):
        self.click(*self.MAC_13)

    def verify_mac_16_page_open(self):
        self.assert_text('MacBook Pro 16-inch', *self.PROD_TITLE)

    def verify_mac_13_page_open(self):
        self.assert_text('MacBook Pro 13-inch', *self.PROD_TITLE)