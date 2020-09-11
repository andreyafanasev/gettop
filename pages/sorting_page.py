from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class Sorting(Page):

    SORT_SELECT = (By.CSS_SELECTOR, 'select.orderby')
    PROD_ORDER = (By.CSS_SELECTOR, 'div.products p.name')

    def sort_by_price_high_to_low(self):
        select = Select(self.find_element(*self.SORT_SELECT))
        select.select_by_value('price-desc')

    def sort_by_price_low_to_high(self):
        select = Select(self.find_element(*self.SORT_SELECT))
        select.select_by_value('price')

    def sort_by_popularity(self):
        select = Select(self.find_element(*self.SORT_SELECT))
        select.select_by_value('popularity')

    def sort_by_rating(self):
        select = Select(self.find_element(*self.SORT_SELECT))
        select.select_by_value('rating')

    def sort_by_latest(self):
        select = Select(self.find_element(*self.SORT_SELECT))
        select.select_by_value('date')

    def verify_sorted_by_price_high_to_low(self):
        expected_order = ['MacBook Pro 16-inch', 'MacBook Pro 13-inch', 'MacBook Air']
        actual_order = [e.text for e in self.find_elements(*self.PROD_ORDER)]
        assert actual_order == expected_order, f'Expected order {expected_order}, but got {actual_order}'

    def verify_sorted_by_price_low_to_high(self):
        expected_order = ['MacBook Air', 'MacBook Pro 13-inch', 'MacBook Pro 16-inch']
        actual_order = [e.text for e in self.find_elements(*self.PROD_ORDER)]
        assert actual_order == expected_order, f'Expected order {expected_order}, but got {actual_order}'

    def verify_sorted_by_popularity(self):
        expected_order = ['MacBook Pro 16-inch', 'MacBook Pro 13-inch', 'MacBook Air']
        actual_order = [e.text for e in self.find_elements(*self.PROD_ORDER)]
        assert actual_order == expected_order, f'Expected order {expected_order}, but got {actual_order}'

    def verify_sorted_by_rating(self):
        expected_order = ['MacBook Pro 16-inch', 'MacBook Pro 13-inch', 'MacBook Air']
        actual_order = [e.text for e in self.find_elements(*self.PROD_ORDER)]
        assert actual_order == expected_order, f'Expected order {expected_order}, but got {actual_order}'

    def verify_sorted_by_latest(self):
        expected_order = ['MacBook Air', 'MacBook Pro 16-inch', 'MacBook Pro 13-inch']
        actual_order = [e.text for e in self.find_elements(*self.PROD_ORDER)]
        assert actual_order == expected_order, f'Expected order {expected_order}, but got {actual_order}'