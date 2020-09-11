from behave import given, when, then


@given('Open {category} Category page')
def open_category_page(context, category):
    context.app.cat.open_category_page(category)


@then('Verify items of correct category (ipad) are shown')
def verify_ipad_category_products(context):
    context.app.cat.verify_ipad_category_products()


@then('"Showing all <N> results" is present and reflects correct amount of items')
def verify_product_amount_ipad_category(context):
    context.app.cat.verify_product_amount_ipad_category()


@then('Verify all items have Category, Name and Price')
def verify_cat_name_price_ipad(context):
    context.app.cat.verify_cat_name_price_ipad()


@then('Verify user can open and close Quick View by clicking on closing X')
def verify_open_close_quick_view(context):
    context.app.cat.verify_open_close_quick_view()


@when('Hover over iPad product')
def hover_over_ipad_prod(context):
    context.app.cat.hover_over_ipad_prod()


@when('Click quick view iPad')
def quick_view_ipad(context):
    context.app.cat.quick_view_ipad()


@then('Verify iPad added to cart')
def verify_ipad_in_cart(context):
    context.app.cat.verify_ipad_in_cart()