from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OutOfStock(Page):
    OUT_OF_ST = (By.CSS_SELECTOR, 'p.out-of-stock')
    CHECK_OUT_BTN = (By.CSS_SELECTOR, 'li.has-dropdown p.buttons a.checkout')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button.single_add_to_cart_button')

    def verify_out_of_stock(self):
        self.assert_text('Out of stock', *self.OUT_OF_ST)

    def verify_add_cart_not_shown(self):
        self.driver.wait.until(EC.invisibility_of_element_located(self.ADD_TO_CART_BTN))

    def verify_checkout_not_shown(self):
        self.driver.wait.until(EC.invisibility_of_element_located(self.CHECK_OUT_BTN))