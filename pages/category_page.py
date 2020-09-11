from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Category(Page):

    PRODUCTS_NAMES = (By.CSS_SELECTOR, 'p.product-title')
    PRODUCTS_CATEGORIES = (By.CSS_SELECTOR, 'p.category')
    PRODUCTS_PRICES = (By.CSS_SELECTOR, 'span.price')
    ALL_PRODUCTS = (By.CSS_SELECTOR, 'div.products div.product')
    AMOUNT_COUNTER = (By.CSS_SELECTOR, 'p.woocommerce-result-count')
    QUICK_VIEW_LNK = (By.CSS_SELECTOR, 'a.quick-view')
    QUICK_VIEW_BOX = (By.CSS_SELECTOR, 'div.product-quick-view-container')
    CLOSE_QV_BTN = (By.CSS_SELECTOR, 'button.mfp-close')
    IPAD = (By.CSS_SELECTOR, 'div.post-186')
    IPAD_QV = (By.CSS_SELECTOR, 'div.post-186 a.quick-view')
    PROD_IN_CART = (By.CSS_SELECTOR, 'td.product-name')

    def open_category_page(self, category):
        self.open_page(f'product-category/{category}/')

    def verify_ipad_category_products(self):
        expected_products = ['iPad', 'iPad Air', 'iPad mini', 'iPad Pro']
        actual_product = [product.text for product in self.find_elements(*self.PRODUCTS_NAMES)]
        assert actual_product == expected_products, f'Expected products {expected_products}, but got {actual_product}'

    def verify_product_amount_ipad_category(self):
        amount_counter = self.find_element(*self.AMOUNT_COUNTER).text
        amount_shown = self.find_elements(*self.ALL_PRODUCTS)
        assert f'Showing all {len(amount_shown)} results' == amount_counter, \
            f'Expected Showing all {len(amount_shown)} results, but got {amount_counter}'

    def verify_cat_name_price_ipad(self):
        all_prod = self.find_elements(*self.ALL_PRODUCTS)
        cat = self.find_elements(*self.PRODUCTS_CATEGORIES)
        names = self.find_elements(*self.PRODUCTS_NAMES)
        price = self.find_elements(*self.PRODUCTS_PRICES)
        assert len(all_prod) == len(cat) == len(names) == len(price)

    def verify_open_close_quick_view(self):
        all_prod = self.find_elements(*self.ALL_PRODUCTS)
        qv_lnk = self.find_elements(*self.QUICK_VIEW_LNK)
        for i in range(len(all_prod)):
            self.actions.move_to_element(all_prod[i]).perform()
            qv_lnk[i].click()
            self.driver.wait.until(EC.visibility_of_element_located(self.QUICK_VIEW_BOX))
            self.click(*self.CLOSE_QV_BTN)
            self.driver.wait.until(EC.invisibility_of_element_located(self.QUICK_VIEW_BOX))

    def hover_over_ipad_prod(self):
        e = self.find_element(*self.IPAD)
        self.actions.move_to_element(e).perform()

    def quick_view_ipad(self):
        self.click(*self.IPAD_QV)

    def verify_ipad_in_cart(self):
        prod = self.find_element(*self.PROD_IN_CART).text
        assert prod == 'iPad', f'Expected product in cart iPad, but got {prod}'