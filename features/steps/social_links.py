from behave import given, when, then


@when('Click Facebook link')
def click_fb_link(context):
    context.app.sl.click_fb_link()


@when('Click Twitter link')
def click_twitter_link(context):
    context.app.sl.click_twitter_link()


@when('Click Email link')
def click_email_link(context):
    context.app.sl.click_email_link()


@when('Click Pinterest link')
def click_pinterest_link(context):
    context.app.sl.click_pinterest_link()


@when('Click LinkedIn link')
def click_linkedin_link(context):
    context.app.sl.click_linkedin_link()


@then('Verify a new window to login to Facebook opens')
def verify_fb_page(context):
    context.app.sl.verify_fb_page()


@then('Verify a new window to login to Twitter opens')
def verify_twitter_page(context):
    context.app.sl.verify_twitter_page()


@then('Verify a new window to login to Email opens')
def verify_email_page(context):
    context.app.sl.verify_email_page()


@then('Verify a new window to login to Pinterest opens')
def verify_pinterest_page(context):
    context.app.sl.verify_pinterest_page()


@then('Verify a new window to login to LinkedIn opens')
def verify_linkedin_page(context):
    context.app.sl.verify_linkedin_page()