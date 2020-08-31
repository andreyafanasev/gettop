from behave import given, when, then
from selenium.webdriver.common.by import By


BANNER_1 = (By.XPATH, "//a[@href='/product-category/ipad/']")
CATEG = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb')


@when('Click on banner 1')
def click_on_banner(context):
    context.app.page.click(*BANNER_1)


@then('Verify if taken to correct category page - {categ}')
def verify_category(context, categ):
    txt = context.driver.find_element(*CATEG).text
    assert categ in txt, f'Expected category - {categ}, but got {txt}'