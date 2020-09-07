from behave import given, when, then
from selenium.webdriver.common.by import By


@when('Click Logo')
def click_logo(context):
    context.app.top.click_logo()


@then('Verify logo clickable and takes to https://gettop.us/')
def verify_page(context):
    context.app.top.verify_page()