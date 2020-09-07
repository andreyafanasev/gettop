from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@when('Hover over Search icon')
def hover_over_search(context):
    context.app.search.hover_over_search()


@when('Enter "{search_item}" in search field')
def search_for(context, search_item):
    context.app.search.search_for(search_item)


@when('Click Submit search')
def submit_search(context):
    context.app.search.submit_search()


@then('Verify "{search_item}" presented')
def verify_search_page(context, search_item):
    context.app.search.verify_search_page(search_item)


@then('Verify "No products were found matching your selection" text presented')
def verify_search_wrong(context):
    context.app.search.verify_search_wrong()