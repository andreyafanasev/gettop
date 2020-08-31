from  behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


PRICE = (By.CSS_SELECTOR, 'div.price-wrapper')
DESCR = (By.CSS_SELECTOR, 'div.product-short-description')


@then('Verify "MacBook Pro 13-inch" has price')
def verify_price(context):
    context.driver.find_element(*PRICE)


@then('Verify "MacBook Pro 13-inch" has description')
def verify_price(context):
    context.driver.find_element(*DESCR)


@then('Verify "iPhone SE" has price')
def verify_price(context):
    context.driver.find_element(*PRICE)


@then('Verify "iPhone SE" has description')
def verify_price(context):
    context.driver.find_element(*DESCR)


@then('Verify "iPad mini" has price')
def verify_price(context):
    context.driver.find_element(*PRICE)


@then('Verify "iPad mini" has description')
def verify_price(context):
    context.driver.find_element(*DESCR)


@then('Verify "Watch Series 5" has price')
def verify_price(context):
    context.driver.find_element(*PRICE)


@then('Verify "Watch Series 5" has description')
def verify_price(context):
    context.driver.find_element(*DESCR)