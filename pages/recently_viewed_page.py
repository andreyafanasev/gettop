from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RecentlyViewed(Page):

    RECENTLY_VIEWED_LNK = (By.CSS_SELECTOR, '#woocommerce_recently_viewed_products-8 a')

    def open_category_page(self, category):
        self.open_page(f'product-category/{category}/')

    def verify_recently_viewed_macbook(self):
        self.driver.wait.until(EC.presence_of_element_located(self.RECENTLY_VIEWED_LNK))

    def click_recently_viewed_macbook_air(self):
        self.click(*self.RECENTLY_VIEWED_LNK)