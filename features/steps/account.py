from behave import given,when, then
from selenium.webdriver.common.by import By


@when('Click Account icon')
def click_account(context):
    context.app.account.click_account()


@then('Verify Login form opens')
def verify_login_form_open(context):
    context.app.account.verify_login_form_open()