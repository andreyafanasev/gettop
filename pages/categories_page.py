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

    TOP_CAT_ACCESS = (By.ID, 'menu-item-472')
    TOP_CAT_IPAD = (By.ID, 'menu-item-470')
    TOP_CAT_IPHONE = (By.ID, 'menu-item-469')
    TOP_CAT_MAC = (By.ID, 'menu-item-468')
    TOP_CAT_WATCH = (By.ID, 'menu-item-471')

    CAT_MAC_PROD = (By.CSS_SELECTOR, '#menu-item-468 ul li')
    CAT_IPHONE_PROD = (By.CSS_SELECTOR, '#menu-item-469 ul li')
    CAT_IPAD_PROD = (By.CSS_SELECTOR, '#menu-item-470 ul li')
    CAT_WATCH_PROD = (By.CSS_SELECTOR, '#menu-item-471 ul li')
    CAT_ACCESS_PROD = (By.CSS_SELECTOR, '#menu-item-472 ul li')

    MACBOOK_AIR = (By.ID, 'menu-item-379')
    IPHONE_11_PRO = (By.ID, 'menu-item-383')
    IPAD_PRO = (By.ID, 'menu-item-391')
    WATCH_S5 = (By.ID, 'menu-item-384')
    AIR_PODS_PRO = (By.ID, 'menu-item-386')
    PROD_TITLE = (By.CSS_SELECTOR, 'h1.product_title')

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

    def hover_over_mac(self):
        mac = self.driver.find_element(*self.TOP_CAT_MAC)
        self.actions.move_to_element(mac).perform()

    def hover_over_iphone(self):
        iphone = self.driver.find_element(*self.TOP_CAT_IPHONE)
        self.actions.move_to_element(iphone).perform()

    def hover_over_ipad(self):
        ipad = self.driver.find_element(*self.TOP_CAT_IPAD)
        self.actions.move_to_element(ipad).perform()

    def hover_over_watch(self):
        watch = self.driver.find_element(*self.TOP_CAT_WATCH)
        self.actions.move_to_element(watch).perform()

    def hover_over_accessories(self):
        access = self.driver.find_element(*self.TOP_CAT_ACCESS)
        self.actions.move_to_element(access).perform()

    def verify_categories_mac(self):
        e = self.find_elements(*self.CAT_MAC_PROD)
        for i in range(len(e)):
            txt = e[i].text
            assert "MacBook" in txt, f'expected text "MacBook", but got {txt}'

    def verify_categories_iphone(self):
        e = self.find_elements(*self.CAT_IPHONE_PROD)
        for i in range(len(e)):
            txt = e[i].text
            assert "iPhone" in txt, f'expected text "iPhone", but got {txt}'

    def verify_categories_ipad(self):
        e = self.find_elements(*self.TOP_CAT_IPAD)
        for i in range(len(e)):
            txt = e[i].text
            assert "iPad" in txt, f'expected text "iPad", but got {txt}'

    def verify_categories_watch(self):
        e = self.find_elements(*self.TOP_CAT_WATCH)
        for i in range(len(e)):
            txt = e[i].text
            assert "Watch" in txt, f'expected text "Watch", but got {txt}'

    def verify_categories_accessories(self):
        e = self.find_elements(*self.TOP_CAT_ACCESS)
        for i in range(len(e)):
            txt = e[i].text
            assert "AirPods" in txt, f'expected text "AirPods", but got {txt}'

    def click_macbook_air(self):
        self.click(*self.MACBOOK_AIR)

    def verify_macbook_air_page(self):
        self.assert_text('MacBook Air', *self.PROD_TITLE)

    def click_iphone_11_pro(self):
        self.click(*self.IPHONE_11_PRO)

    def verify_iphone_11_pro_page(self):
        self.assert_text('iPhone 11 Pro', *self.PROD_TITLE)

    def click_ipad_pro(self):
        self.click(*self.IPAD_PRO)

    def verify_ipad_pro_page(self):
        self.assert_text('iPad Pro', *self.PROD_TITLE)

    def click_watch_s5(self):
        self.click(*self.WATCH_S5)

    def verify_watch_s5_page(self):
        self.assert_text('Watch Series 5', *self.PROD_TITLE)

    def click_airpods_pro(self):
        self.click(*self.AIR_PODS_PRO)

    def verify_airpods_pro_page(self):
        self.assert_text('AirPods Pro', *self.PROD_TITLE)