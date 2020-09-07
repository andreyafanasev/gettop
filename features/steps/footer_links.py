from behave import given, when, then
from selenium.webdriver.common.by import By


@then('Verify footer shows Best Selling, Latest, Top Rated categories')
def verify_bs_latest_top(context):
    context.app.footer.verify_bs_latest_top()


@then('Verify All products in the footer have price, name, star-rating')
def verify_price_name_star(context):
    context.app.footer.verify_price_name_star()


@then('Verify "Copyright 2020" shown in footer')
def verify_copyright(context):
    context.app.footer.verify_copyright()


@then('Verify Footer has button to go back to top')
def verify_go_top_btn(context):
    context.app.footer.verify_go_top_btn()


@then('Verify Footer has working links to all product categories')
def verify_footer_links(context):
    context.app.footer.verify_footer_links()