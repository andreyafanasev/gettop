from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SALE_ICONS = (By.CSS_SELECTOR, 'div.on-sale')
IMAGE = (By.CSS_SELECTOR, 'img.attachment-woocommerce_thumbnail')
CATEG = (By.CSS_SELECTOR, 'p.category')
NAME = (By.CSS_SELECTOR, 'p.name.product-title')
PRICE = (By.CSS_SELECTOR, 'span.price')
STAR_RATING = (By.CSS_SELECTOR, 'div.price-wrapper div.star-rating')
PRODUCT = (By.CSS_SELECTOR, 'div.slider-nav-reveal.slider-nav-push div.product-small.col')


@then('Verify Every product has Sale icon, image, product category, name, price, and star-rating')
def verify_sale_icon(context):
    product = context.driver.find_elements(*PRODUCT)
    for i in product:
        i.find_element(*SALE_ICONS)
        i.find_element(*IMAGE)
        i.find_element(*CATEG)
        i.find_element(*NAME)
        i.find_element(*PRICE)
        i.find_element(*STAR_RATING)