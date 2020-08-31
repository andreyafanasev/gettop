from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


RIGHT_ARROW = (By.CSS_SELECTOR, 'div.slider-nav-circle button.next')
LEFT_ARROW = (By.CSS_SELECTOR, 'div.slider-nav-circle button.previous')
BANNER = (By.CSS_SELECTOR, 'div.fill.banner-link')


@given('Open home page')
def open_home_page(context):
    context.app.page.open_page()


@then('Verify that user can click right arrow')
def verify_presence_right_banner(context):
    banners = context.driver.find_elements(*BANNER)
    for i in range(len(banners)):
        context.app.page.click(*RIGHT_ARROW)
        context.driver.wait.until(EC.visibility_of_element_located(BANNER))


@then('Verify that user can click left arrow')
def verify_presence_left_banner(context):
    banners = context.driver.find_elements(*BANNER)
    for i in range(len(banners)):
        context.app.page.click(*LEFT_ARROW)
        context.driver.wait.until(EC.visibility_of_element_located(BANNER))
