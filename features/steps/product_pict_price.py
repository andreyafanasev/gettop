from behave import given, when, then
from selenium.webdriver.common.by import By


@then('Verify product (MacBook Air) has image, name, price, description')
def verify_name_price(context):
    context.app.product.verify_name_price()


@when('Click Zoom button')
def click_zoom_btn(context):
    context.app.product.click_zoom_btn()


@then('Verify User can scroll through images')
def verify_scroll_through_pic(context):
    context.app.product.verify_scroll_through_pic()


@when('Click [x] to close images')
def close_img(context):
    context.app.product.close_img()


@then('Verify images closed')
def verify_pic_closed(context):
    context.app.product.verify_pic_closed()


@when('Hover over MAC picture')
def hover_over_mac_pic(context):
    context.app.product.hover_over_mac_pic()


@when('Click on the heart icon')
def click_heart_icon(context):
    context.app.product.click_heart_icon()


@then('Verify product added to wishlist(message "Product added!" shown)')
def product_added_shown(context):
    context.app.product.product_added_shown()


@when('Click category "Macbook" link')
def click_mac_cat_link(context):
    context.app.product.click_mac_cat_link()


@then('Verify Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn')
def verify_social_links(context):
    context.app.product.verify_social_links()