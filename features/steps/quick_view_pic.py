from behave import given, when, then


@then('Verify that click through "MacBook Pro 13-inch" images')
def verify_click_through_pic(context):
    context.app.quick.verify_click_through_pic_mac()


@then('Verify that click through "iPhone SE" images')
def verify_click_through_pic(context):
    context.app.quick.verify_click_through_pic_iphone()


@then('Verify that click through "iPad mini" images')
def verify_click_through_pic(context):
    context.app.quick.verify_click_through_pic_ipad()


@then('Verify that click through "Watch Series 5" images')
def verify_click_through_pic(context):
    context.app.quick.verify_click_through_pic_watches()