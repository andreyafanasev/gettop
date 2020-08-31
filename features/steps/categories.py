from behave import given, when, then
from selenium.webdriver.common.by import By


@when('Click ACCESSORIES category')
def click_access_cat(context):
    context.app.categories.click_access_cat()


@when('Click IPAD category')
def click_ipad_cat(context):
    context.app.categories.click_ipad_cat()


@when('Click IPHONE category')
def click_iphone_cat(context):
    context.app.categories.click_iphone_cat()


@when('Click MACBOOK category')
def click_mac_cat(context):
    context.app.categories.click_mac_cat()


@then('Verify ACCESSORIES page opens')
def verify_access_cat(context):
    context.app.categories.verify_access_cat()


@then('Verify IPAD page opens')
def verify_ipad_cat(context):
    context.app.categories.verify_ipad_cat()


@then('Verify IPHONE page opens')
def verify_iphone_cat(context):
    context.app.categories.verify_iphone_cat()


@then('Verify MACBOOK page opens')
def verify_mac_cat(context):
    context.app.categories.verify_mac_cat()