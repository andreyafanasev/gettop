from pages.base_page import Page
from selenium.webdriver.common.by import By


class Footer(Page):

    FOOTER_CAT = (By.CSS_SELECTOR, 'span.widget-title')
    FOOTER_ALL_PROD = (By.CSS_SELECTOR, 'div.row li')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'span.product-title')
    STAR_RATING = (By.CSS_SELECTOR, 'div.star-rating')
    PRICE = (By.CSS_SELECTOR, 'span.amount')
    COPYRIGHT = (By.CSS_SELECTOR, 'div.copyright-footer')
    BACK_TO_TOP_BTN = (By.ID, 'top-link')
    FOOTER_LINKS = (By.CSS_SELECTOR, '#menu-main-1 a')
    HEADER = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb')

    def verify_bs_latest_top(self):
        expect_cat = ['BEST SELLING', 'LATEST', 'TOP RATED']
        cat = self.find_elements(*self.FOOTER_CAT)
        for i in range(len(cat)):
            cat_txt = cat[i].text
            assert cat_txt == expect_cat[i], f'Expected category - {expect_cat[i]}, actual category {cat_txt}'

    def verify_price_name_star(self):
        all_prod = self.find_elements(*self.FOOTER_ALL_PROD)
        for i in range(len(all_prod)):
            e = all_prod[i]
            e.find_element(*self.PRODUCT_NAME)
            e.find_element(*self.STAR_RATING)
            e.find_element(*self.PRICE)

    def verify_copyright(self):
        self.assert_text('Copyright 2020', *self.COPYRIGHT)

    def verify_go_top_btn(self):
        self.find_element(*self.BACK_TO_TOP_BTN)

    def verify_footer_links(self):
        links = self.find_elements(*self.FOOTER_LINKS)
        needed_cat = ['MAC', 'IPHONE', 'IPAD', 'WATCH', 'ACCESSORIES']
        for i in range(len(links)):
            links = self.find_elements(*self.FOOTER_LINKS)
            links[i].click()
            self.assert_text(needed_cat[i], *self.HEADER)
