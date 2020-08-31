from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class HomePage(Page):

    PRODUCT = (By.CSS_SELECTOR, 'div.product-small.col')
    HEART_ICON = (By.CSS_SELECTOR, 'i.icon-heart')
    MESSAGE = (By.ID, 'yith-wcwl-popup-message')


    def hover_product(self):
        product = self.find_elements(*self.PRODUCT)
        heart = self.find_elements(*self.HEART_ICON)
        for i in range(len(product)):
            prod_to_hov = product[i]
            self.actions.move_to_element(prod_to_hov).perform()
            heart[i].click()
            sleep(2)
            txt = self.driver.find_element(*self.MESSAGE).text
            assert txt == 'Product added!', f'Expected message "Product added!", but got {txt}'
            sleep(2)