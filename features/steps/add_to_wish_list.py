from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


HEART_ICON_1 = (By.CSS_SELECTOR, 'div.wishlist-icon')
MESSAGE = (By.ID, 'yith-wcwl-popup-message')
PRODUCT_1 = (By.CSS_SELECTOR, 'div.slider-nav-reveal.slider-nav-push div.product-small.col')


@then('Hover over product, click on heart icon to add to wishlist')
def hover_product(context):
    context.app.home.hover_product()