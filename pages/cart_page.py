from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Cart(Page):

    CART_ICON = (By.CSS_SELECTOR, 'li.cart-item.has-dropdown')
    EMPTY_CART_TXT = (By.CSS_SELECTOR, 'p.cart-empty')
    EMPTY_CART_HEADER_TXT = (By.CSS_SELECTOR, 'li.html.widget_shopping_cart')
    PRICE_IN_CART = (By.CSS_SELECTOR, 'td.product-price')
    COUNTER = (By.CSS_SELECTOR, 'div.hide-for-medium.flex-right span.cart-icon')
    PROD_IN_CART = (By.CSS_SELECTOR, 'li.has-dropdown li.woocommerce-mini-cart-item')
    SUBTOTAL = (By.CSS_SELECTOR, 'li.has-dropdown p.total')
    VIEW_CART_BTN = (By.CSS_SELECTOR, "li.has-dropdown p.buttons a[href='https://gettop.us/cart/']")
    CHECK_OUT_BTN = (By.CSS_SELECTOR, 'li.has-dropdown p.buttons a.checkout')
    # CART_PAGE = (By.CSS_SELECTOR, 'a.current')
    REMOVE_BTN = (By.CSS_SELECTOR, 'li.has-dropdown a.remove')

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def verify_empty_cart_page(self):
        self.assert_text('Your cart is currently empty.', *self.EMPTY_CART_TXT)

    def hover_over_cart(self):
        cart = self.driver.find_element(*self.CART_ICON)
        self.actions.move_to_element(cart).perform()

    def verify_text_empty_cart(self):
        self.assert_text('No products in the cart.', *self.EMPTY_CART_HEADER_TXT)

    def verify_price_mac_pro(self):
        self.assert_text('$349.00', *self.PRICE_IN_CART)

    def verify_amount(self):
        txt = self.driver.find_element(*self.COUNTER).text
        assert txt == '1', f'Expected counter increased by 1, but it was increased by {txt}'

    def verify_product_total_ipad(self):
        self.assert_text('iPad', *self.PROD_IN_CART)
        subtotal = self.find_element(*self.SUBTOTAL).text
        assert subtotal == 'Subtotal: $349.00', f'Expected subtotal $349.00, but got {subtotal}'

    def click_view_cart(self):
        self.click(*self.VIEW_CART_BTN)

    def verify_cart_open(self):
        car_url = self.driver.current_url
        assert car_url == 'https://gettop.us/cart/', f'Current URL {car_url}'

    def click_check_out(self):
        self.click(*self.CHECK_OUT_BTN)

    def verify_check_out_open(self):
        car_url = self.driver.current_url
        assert car_url == 'https://gettop.us/checkout/', f'Current URL {car_url}'

    def verify_product_removed(self):
        self.click(*self.REMOVE_BTN)
        self.driver.wait.until(EC.invisibility_of_element_located(self.PROD_IN_CART))


