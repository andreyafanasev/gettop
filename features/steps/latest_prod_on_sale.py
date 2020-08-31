from behave import given, when, then
from selenium.webdriver.common.by import By


TXT = (By.XPATH, "//*[text()='Latest products on sale']")


@then('Verify that {given_text} text is shown')
def verify_text(context, given_text):
    context.app.page.assert_text(given_text, *TXT)

