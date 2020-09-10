from behave import given, when,then
from time import sleep


@given('Open {product} product page')
def open_prod_page(context, product):
    context.app.add.open_prod_page(product)


@when('Click + to increase amount of items to add to cart')
def click_plus_btn(context):
    context.app.add.click_plus_btn()


@then('Verify that amount of items (2) shown in top nav menu are correct')
def verify_amount_mac(context):
    context.app.add.verify_amount_mac()


@when('Click "-" to decrease amount of items to add to cart')
def click_minus_btn(context):
    context.app.add.click_minus_btn()


@when('Type in amount of items to add to cart (2)')
def type_in_amount(context):
    context.app.add.type_in_amount()


@then('Verify MacBook Pro 13-inch has been added to your cart message is shown')
def conf_mac_shown(context):
    context.app.add.conf_mac_shown()