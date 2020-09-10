from behave import given, when, then
from selenium.webdriver.common.by import By


@then('Verify "Out of Stock" sign is shown')
def verify_out_of_stock(context):
    context.app.out.verify_out_of_stock()


@then('Verify "Add to Cart" button is not shown')
def verify_add_cart_not_shown(context):
    context.app.out.verify_add_cart_not_shown()


@then('Verify "Checkout" button is not shown')
def verify_checkout_not_shown(context):
    context.app.out.verify_checkout_not_shown()