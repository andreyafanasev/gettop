from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

MAC = (By.CSS_SELECTOR, 'div.product_tag-macbook')
IPHONE = (By.CSS_SELECTOR, 'div.product_cat-iphone')
IPAD = (By.CSS_SELECTOR, 'div.product_cat-ipad')
WATCH = (By.CSS_SELECTOR, 'div.product_cat-watch')
ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button.single_add_to_cart_button')
CART = (By.CSS_SELECTOR, 'span.header-cart-title')
PRODUCT_IN_CART = (By.CSS_SELECTOR, 'td.product-name')


@when('Click on product "MacBook Pro 13-inch" on sale')
def click_on_product(context):
    context.app.page.click(*MAC)


@when('Click on product "iPhone SE" on sale')
def click_on_product(context):
    context.app.page.click(*IPHONE)


@when('Click on product "iPad mini" on sale')
def click_on_product(context):
    context.app.page.click(*IPAD)


@when('Click on product "Watch Series 5" on sale')
def click_on_product(context):
    context.app.page.click(*WATCH)


@when('Click add to cart button')
def click_add_to_cart(context):
    context.app.page.click(*ADD_TO_CART_BTN)


@when('Open the cart')
def open_cart(context):
    context.app.page.click(*CART)


@then('Verify "MacBook Pro 13-inch" added to cart')
def verify_product_in_cart(context):
    context.app.page.assert_text('MacBook Pro 13-inch', *PRODUCT_IN_CART)


@then('Verify "iPhone SE" added to cart')
def verify_product_in_cart(context):
    context.app.page.assert_text('iPhone SE', *PRODUCT_IN_CART)


@then('Verify "iPad mini" added to cart')
def verify_product_in_cart(context):
    context.app.page.assert_text('iPad mini', *PRODUCT_IN_CART)


@then('Verify "Watch Series 5" added to cart')
def verify_product_in_cart(context):
    context.app.page.assert_text('Watch Series 5', *PRODUCT_IN_CART)