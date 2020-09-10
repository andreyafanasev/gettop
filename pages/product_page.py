from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Product(Page):

    IMG = (By.CSS_SELECTOR, 'div.slide.is-selected img')
    NAME = (By.CSS_SELECTOR, 'h1.product-title')
    PRICE = (By.CSS_SELECTOR, 'div.price-wrapper')
    DESCR = (By.CSS_SELECTOR, 'div.product-short-description')

    ZOOM = (By.CSS_SELECTOR, 'div.bottom')
    BTN_RIGHT = (By.CSS_SELECTOR, 'button.pswp__button--arrow--right')
    BTN_LEFT = (By.CSS_SELECTOR, 'button.pswp__button--arrow--left')
    PIC = (By.CSS_SELECTOR, 'img.pswp__img')
    CLOSE_PIC = (By.CSS_SELECTOR, 'button.pswp__button--close')
    PIC_MAIN = (By.CSS_SELECTOR, 'div.woocommerce-product-gallery__image.first')
    HEART_ICON = (By.CSS_SELECTOR, 'div.wishlist-icon')
    MSG = (By.ID, 'yith-wcwl-popup-message')

    CAT_LINK = (By.CSS_SELECTOR, 'span.posted_in a')

    SOCIAL_LNKS = (By.CSS_SELECTOR, 'div.social-icons.relative a')

    RIGHT_ARROW = (By.CSS_SELECTOR, '#product-sidebar i.icon-angle-right')
    LEFT_ARROW = (By.CSS_SELECTOR, '#product-sidebar i.icon-angle-left')
    PROD_TITLE = (By.CSS_SELECTOR, 'h1.product_title')

    def verify_name_price(self):
        self.find_element(*self.IMG)
        self.find_element(*self.NAME)
        self.find_element(*self.PRICE)
        self.find_element(*self.DESCR)

    def click_zoom_btn(self):
        self.click(*self.ZOOM)

    def verify_scroll_through_pic(self):
        pic = self.find_elements(*self.PIC)
        for i in range(len(pic)):
            self.click(*self.BTN_RIGHT)
            self.driver.wait.until(EC.presence_of_element_located(self.PIC))
        for i in range(len(pic)):
            self.click(*self.BTN_RIGHT)
            self.driver.wait.until(EC.presence_of_element_located(self.PIC))

    def close_img(self):
        self.click(*self.CLOSE_PIC)

    def verify_pic_closed(self):
        self.driver.wait.until_not(EC.visibility_of_element_located(self.PIC))

    def hover_over_mac_pic(self):
        mac_pic = self.find_element(*self.PIC_MAIN)
        self.actions.move_to_element(mac_pic).perform()

    def click_heart_icon(self):
        self.click(*self.HEART_ICON)

    def product_added_shown(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.MSG))
        txt = self.find_element(*self.MSG).text
        assert txt == 'Product added!', f'Expected: Product added, but got {txt}'

    def click_mac_cat_link(self):
        self.click(*self.CAT_LINK)

    def verify_social_links(self):
        self.find_elements(*self.SOCIAL_LNKS)

    def click_back_prod_arrow(self):
        self.click(*self.LEFT_ARROW)

    def click_forward_prod_arrow(self):
        self.click(*self.RIGHT_ARROW)

    def verify_mac_16_page_open(self):
        self.assert_text('MacBook Pro 16-inch', *self.PROD_TITLE)

    def verify_mac_13_page_open(self):
        self.assert_text('MacBook Pro 13-inch', *self.PROD_TITLE)