from behave import given, when, then


@then('Verify "You may also like…" bock is shown')
def verify_may_like_shown(context):
    context.app.you.verify_may_like_shown()


@then('Verify "You may also like…" bock contains products')
def verify_you_may_prod_title(context):
    context.app.you.verify_you_may_prod_title()


@when('Click MacBook Pro 16 inch product link')
def click_mac_pro_16(context):
    context.app.you.click_mac_pro_16()


@when('Click MacBook Pro 13 inch product link')
def click_mac_pro_13(context):
    context.app.you.click_mac_pro_13()


@then('Verify MacBook Pro 16 inch product page opens')
def verify_mac_16_page_open(context):
    context.app.you.verify_mac_16_page_open()


@then('Verify MacBook Pro 13 inch product page opens')
def verify_mac_13_page_open(context):
    context.app.you.verify_mac_13_page_open()