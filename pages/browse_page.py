from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Browse(Page):

    BROWSE_LNK = (By.CSS_SELECTOR, 'ul.product-categories a')
    CATEGORY_NAME = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb')

    def verify_browse_category(self):
        expected_categ = ['Accessories', 'AirPods', 'Watch', 'iPad', 'iPhone', 'MacBook']
        category = [e.text for e in self.find_elements(*self.BROWSE_LNK)]
        assert expected_categ == category, f'Expected categories {expected_categ}, but got {category}'

    def verify_click_browse_category(self):
        browse_cat = self.find_elements(*self.BROWSE_LNK)
        for i in range(len(browse_cat)):
            browse_cat[i].click()
            browse_cat = self.find_elements(*self.BROWSE_LNK)
            expected_name = browse_cat[i].text
            cat_name = self.find_element(*self.CATEGORY_NAME).text
            assert expected_name.upper() in cat_name, f'Expected open category {expected_name}, but got {cat_name}'