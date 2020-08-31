from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# QUICK_VEW_LINKS = (By.CSS_SELECTOR, 'a.quick-view')
QUICK_VEW_MAC = (By.CSS_SELECTOR, 'a[data-prod="180"]')
QUICK_VEW_IPHONE = (By.CSS_SELECTOR, 'a[data-prod="167"]')
QUICK_VEW_IPAD = (By.CSS_SELECTOR, 'a[data-prod="179"]')
QUICK_VEW_WATCHES = (By.CSS_SELECTOR, 'a[data-prod="171"]')
ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button.single_add_to_cart_button')


@when('Hover over "MacBook Pro 13-inch"')
def hover_over_product(context):
    context.app.quick.hover_over_mac()


@when('Hover over "iPhone SE"')
def hover_over_product(context):
    context.app.quick.hover_over_iphone()


@when('Hover over "iPad mini"')
def hover_over_product(context):
    context.app.quick.hover_over_ipad()


@when('Hover over "Watch Series 5"')
def hover_over_product(context):
    context.app.quick.hover_over_watches()


@when('Click Quick view "MacBook Pro 13-inch"')
def click_quick_view(context):
    context.app.page.click(*QUICK_VEW_MAC)


@when('Click Quick view "iPhone SE"')
def click_quick_view(context):
    context.app.page.click(*QUICK_VEW_IPHONE)


@when('Click Quick view "iPad mini"')
def click_quick_view(context):
    context.app.page.click(*QUICK_VEW_IPAD)


@when('Click Quick view "Watch Series 5"')
def click_quick_view(context):
    context.app.page.click(*QUICK_VEW_WATCHES)


@then('Verify Quick view is open')
def verify_quick_view_open(context):
    context.app.quick.verify_quick_view_open()


@when('Click X to close Quick view')
def close_quick_view(context):
    context.app.quick.close_quick_view()


@then('Verify Quick view closed')
def verify_quick_view_closed(context):
    context.app.quick.verify_quick_view_closed()


