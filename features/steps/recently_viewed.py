from behave import when, then


@when('Open {category} Category page')
def open_category_page(context, category):
    context.app.recently.open_category_page(category)


@then('Verify User can see recently viewed item (Macbook Air)')
def verify_recently_viewed_macbook(context):
    context.app.recently.verify_recently_viewed_macbook()


@when('Click recently viewed item (Macbook Air)')
def click_recently_viewed_macbook_air(context):
    context.app.recently.click_recently_viewed_macbook_air()