from pages.base_page import Page
from selenium.webdriver.common.by import By


class AddingToCart(Page):

    PLUS_BTN = (By.CSS_SELECTOR, 'input.plus.button')
    MINUS_BTN = (By.CSS_SELECTOR, 'input.minus.button')
    INPUT = (By.CSS_SELECTOR, 'input.qty')
    COUNTER = (By.CSS_SELECTOR, 'div.hide-for-medium.flex-right span.cart-icon')
    CONFIRM = (By.CSS_SELECTOR, 'div.message-container')

    def open_prod_page(self, product):
        self.open_product_page(f'product/{product}')

    def click_plus_btn(self):
        self.click(*self.PLUS_BTN)

    def click_minus_btn(self):
        self.click(*self.MINUS_BTN)

    def verify_amount_mac(self):
        txt = self.find_element(*self.COUNTER).text
        assert txt == '2', f'Expected amount 2, but got {txt}'

    def type_in_amount(self):
        self.input(2, *self.INPUT)

    def conf_mac_shown(self):
        txt = self.find_element(*self.CONFIRM).text
        assert txt == '“MacBook Pro 13-inch” has been added to your cart.', f'Expected text "“MacBook Pro 13-inch” has been added to your cart.", but got {txt}'