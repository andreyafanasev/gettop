from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


DOTS = (By.CSS_SELECTOR, 'ol.flickity-page-dots li')
BANNER = (By.CSS_SELECTOR, 'div.fill.banner-link')


@then('Verify that user can click bottom dots to see top banners')
def verify_dots(context):
    dots = context.driver.find_elements(*DOTS)
    for i in range(len(dots)):
        dot_for_click = context.driver.find_elements(*DOTS)
        dot_for_click[i].click()
        context.driver.wait.until(EC.visibility_of_element_located(BANNER))