from behave import when, then


@when('Slide left dot of the price slider 50% to the right')
def slide_left_knob_to_right(context):
    context.app.filter.slide_left_knob_to_right()


@when('Apply filter (Click Filter btn)')
def click_filter_btn(context):
    context.app.filter.click_filter_btn()


@then('Verify correct products for category macbook (after filter applying) are presented')
def verify_product_filter(context):
    context.app.filter.verify_product_filter()


@when('Reset price filter')
def reset_price_filter(context):
    context.app.filter.reset_price_filter()


@then('Verify correct products for category macbook (after filter reset) are presented')
def verify_product_filter_reset(context):
    context.app.filter.verify_product_filter_reset()


@when('Slide left dot of the price slider 100% to the right')
def slide_left_knob_all_way_right(context):
    context.app.filter.slide_left_knob_all_way_right()


@then('Verify "No products were found matching your selection." message shown')
def verify_no_prod_message(context):
    context.app.filter.verify_no_prod_message()