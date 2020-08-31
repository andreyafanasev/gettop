from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class QuickView(Page):

    MAC = (By.CSS_SELECTOR, 'div.product_tag-macbook')
    IPHONE = (By.CSS_SELECTOR, 'div.product_cat-iphone')
    IPAD = (By.CSS_SELECTOR, 'div.product_cat-ipad')
    WATCHES = (By.CSS_SELECTOR, 'div.product_cat-watch')
    QV_CONT = (By.CSS_SELECTOR, 'div.product-quick-view-container')
    CLOSE_Q_V = (By.CSS_SELECTOR, 'button.mfp-close')
    PIC = (By.CSS_SELECTOR, 'div.slide.is-selected')
    NEXT_BTN = (By.CSS_SELECTOR, 'div.product-gallery div button.next')
    ALL_PIC_MAC = (By.CSS_SELECTOR, 'div#product-180 div div.slider div.slide')
    ALL_PIC_IPHONE = (By.CSS_SELECTOR, 'div#product-167 div div.slider div.slide')
    ALL_PIC_IPAD = (By.CSS_SELECTOR, 'div#product-179 div.slider div.slide')
    ALL_PIC_WATCHES = (By.CSS_SELECTOR, 'div#product-171 div div.slider div.slide')

    def hover_over_mac(self):
        mac = self.driver.find_element(*self.MAC)
        self.actions.move_to_element(mac).perform()

    def hover_over_iphone(self):
        iphone = self.driver.find_element(*self.IPHONE)
        self.actions.move_to_element(iphone).perform()

    def hover_over_ipad(self):
        ipad = self.driver.find_element(*self.IPAD)
        self.actions.move_to_element(ipad).perform()

    def hover_over_watches(self):
        watches = self.driver.find_element(*self.WATCHES)
        self.actions.move_to_element(watches).perform()

    def verify_quick_view_open(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.QV_CONT))

    def close_quick_view(self):
        self.click(*self.CLOSE_Q_V)

    def verify_quick_view_closed(self):
        self.driver.wait.until(EC.invisibility_of_element_located(self.QV_CONT))

    def verify_click_through_pic_mac(self):
        pic = self.driver.find_elements(*self.ALL_PIC_MAC)
        for i in range(len(pic)):
            self.click(*self.NEXT_BTN)
            self.driver.wait.until(EC.visibility_of_element_located(self.PIC))

    def verify_click_through_pic_iphone(self):
        pic = self.driver.find_elements(*self.ALL_PIC_IPHONE)
        for i in range(len(pic)):
            self.click(*self.NEXT_BTN)
            self.driver.wait.until(EC.visibility_of_element_located(self.PIC))

    def verify_click_through_pic_ipad(self):
        pic = self.driver.find_elements(*self.ALL_PIC_IPAD)
        for i in range(len(pic)):
            self.click(*self.NEXT_BTN)
            self.driver.wait.until(EC.visibility_of_element_located(self.PIC))

    def verify_click_through_pic_watches(self):
        pic = self.driver.find_elements(*self.ALL_PIC_WATCHES)
        for i in range(len(pic)):
            self.click(*self.NEXT_BTN)
            self.driver.wait.until(EC.visibility_of_element_located(self.PIC))