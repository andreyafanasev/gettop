from pages.base_page import Page
from selenium.webdriver.common.by import By


class Filter(Page):

    KNOBS = (By.CSS_SELECTOR, 'span.ui-slider-handle')
    FILTER_BTN = (By.XPATH, '//button[text()="Filter"]')
    PROD_ORDER = (By.CSS_SELECTOR, 'div.products p.name')
    RESET_LNKS = (By.CSS_SELECTOR, '#woocommerce_layered_nav_filters-10 a')
    MSG = (By.CSS_SELECTOR, 'p.woocommerce-info')

    def slide_left_knob_to_right(self):
        left_knob = self.find_elements(*self.KNOBS)[0]
        self.actions.click_and_hold(left_knob).move_by_offset(100, 0).perform()

    def click_filter_btn(self):
        self.click(*self.FILTER_BTN)

    def verify_product_filter(self):
        expected_products = ['MacBook Pro 16-inch']
        actual_products = [e.text for e in self.find_elements(*self.PROD_ORDER)]
        assert actual_products == expected_products, f'Expected order {expected_products}, but got {actual_products}'

    def reset_price_filter(self):
        reset_lnk = self.find_elements(*self.RESET_LNKS)
        reset_lnk[0].click()
        reset_lnk = self.find_elements(*self.RESET_LNKS)
        reset_lnk[0].click()

    def verify_product_filter_reset(self):
        expected_products = ['MacBook Air', 'MacBook Pro 13-inch', 'MacBook Pro 16-inch']
        actual_products = [e.text for e in self.find_elements(*self.PROD_ORDER)]
        assert actual_products == expected_products, f'Expected order {expected_products}, but got {actual_products}'

    def slide_left_knob_all_way_right(self):
        left_knob = self.find_elements(*self.KNOBS)[0]
        self.actions.click_and_hold(left_knob).move_by_offset(250, 0).perform()

    def verify_no_prod_message(self):
        msg = self.find_element(*self.MSG).text
        assert msg == 'No products were found matching your selection.', f'Expected message No products were found matching your selection., but got {msg}'