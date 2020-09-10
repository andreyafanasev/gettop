from behave import given, when, then
from selenium.webdriver.common.by import By


@when('Hover over MAC')
def hover_over_mac(context):
    context.app.categories.hover_over_mac()


@then('Verify correct menu options for MAC presented')
def verify_categories_mac(context):
    context.app.categories.verify_categories_mac()


@when('Hover over iPhone')
def hover_over_iphone(context):
    context.app.categories.hover_over_iphone()


@then('Verify correct menu options for iPhone presented')
def verify_categories_iphone(context):
    context.app.categories.verify_categories_iphone()


@when('Hover over iPad')
def hover_over_ipad(context):
    context.app.categories.hover_over_ipad()


@then('Verify correct menu options for iPad presented')
def verify_categories_ipad(context):
    context.app.categories.verify_categories_ipad()


@when('Hover over Watch')
def hover_over_watch(context):
    context.app.categories.hover_over_watch()


@then('Verify correct menu options for Watch presented')
def verify_categories_watch(context):
    context.app.categories.verify_categories_watch()


@when('Hover over Accessories')
def hover_over_accessories(context):
    context.app.categories.hover_over_accessories()


@then('Verify correct menu options for Accessories presented')
def verify_categories_accessories(context):
    context.app.categories.verify_categories_accessories()


@when('Click MacBookAir link')
def click_macbook_air(context):
    context.app.categories.click_macbook_air()


@then('Verify MacBookAir page opens')
def verify_macbook_air_page(context):
    context.app.categories.verify_macbook_air_page()


@when('Click iPhone 11 Pro link')
def click_iphone_11_pro(context):
    context.app.categories.click_iphone_11_pro()


@then('Verify iPhone 11 Pro page opens')
def verify_iphone_11_pro_page(context):
    context.app.categories.verify_iphone_11_pro_page()


@when('Click iPad Pro link')
def click_ipad_pro(context):
    context.app.categories.click_ipad_pro()


@then('Verify iPad Pro page opens')
def verify_ipad_pro_page(context):
    context.app.categories.verify_ipad_pro_page()


@when('Click Watch Series 5 link')
def click_watch_s5(context):
    context.app.categories.click_watch_s5()


@then('Verify Watch Series 5 page opens')
def verify_watch_s5_page(context):
    context.app.categories.verify_watch_s5_page()


@when('Click AirPods Pro link')
def click_airpods_pro(context):
    context.app.categories.click_airpods_pro()


@then('Verify AirPods Pro page opens')
def verify_airpods_pro_page(context):
    context.app.categories.verify_airpods_pro_page()