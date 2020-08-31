from behave import then
from selenium.webdriver.common.by import By

TXT = (By.XPATH, "//*[text()='Browse our Categories']")


@then('Verify "Browse Our Categories" text is shown')
def verify_text(context):
    context.app.page.assert_text('BROWSE OUR CATEGORIES', *TXT)


@then('Verify 4 correct categories are shown')
def verify_categ_shown(context):
    context.app.categories.verify_categ_shown()