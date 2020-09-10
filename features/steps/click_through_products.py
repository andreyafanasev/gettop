from behave import given, when, then


@when('Click back arrow')
def click_back_prod_arrow(context):
    context.app.product.click_back_prod_arrow()


@when('Click forward arrow')
def click_forward_prod_arrow(context):
    context.app.product.click_forward_prod_arrow()


@then('Verify macbook-pro-16 page open')
def verify_mac_16_page_open(context):
    context.app.product.verify_mac_16_page_open()


@then('Verify macbook-pro-13 page open')
def verify_mac_13_page_open(context):
    context.app.product.verify_mac_13_page_open()