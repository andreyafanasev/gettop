from behave import given, when, then
from selenium.webdriver.common.by import By

RIGHT_ARROW = (By.CSS_SELECTOR, 'div.slider-nav-circle button.next')
BANNER_2 = (By.XPATH, '//a[@href="/product-category/macbook/"]')


@when('Click on banner 2')
def click_on_banner(context):
    context.app.page.click(*RIGHT_ARROW)
    context.app.page.click(*BANNER_2)
