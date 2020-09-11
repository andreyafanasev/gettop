from behave import when, then


@then('Verify user sees correct categories under Browse')
def verify_browse_category(context):
    context.app.browse.verify_browse_category()


@then('Verify user can click on categories under Browse and correct page opens')
def verify_click_browse_category(context):
    context.app.browse.verify_click_browse_category()