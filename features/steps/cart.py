from behave import when, then


@when('Click cart icon')
def click_cart_icon(context):
    context.app.cart.click_cart_icon()


@then('Verify Empty cart page opens')
def verify_empty_cart_page(context):
    context.app.cart.verify_empty_cart_page()


@when('Hover over Cart icon')
def hover_over_cart(context):
    context.app.cart.hover_over_cart()


@then('Verify "No products in the cart." message is shown')
def verify_text_empty_cart(context):
    context.app.cart.verify_text_empty_cart()


@then('Verify that price in top nav menu is correct')
def verify_price_mac_pro(context):
    context.app.cart.verify_price_mac_pro()


@then('Verify that amount of items shown in top nav menu are correct')
def verify_amount(context):
    context.app.cart.verify_amount()


@then('Verify correct product - "iPad mini" and subtotal shown')
def verify_product_total_ipad(context):
    context.app.cart.verify_product_total_ipad()


@when('Click VIEW CART button')
def click_view_cart(context):
    context.app.cart.click_view_cart()


@then('Verify cart page is open')
def verify_cart_open(context):
    context.app.cart.verify_cart_open()


@when('Click CHECK OUT button')
def click_check_out(context):
    context.app.cart.click_check_out()


@then('Verify CHECK OUT page is open')
def verify_check_out_open(context):
    context.app.cart.verify_check_out_open()


@when('Click REMOVE BTN [X]')
def verify_product_removed(context):
    context.app.cart.verify_product_removed()