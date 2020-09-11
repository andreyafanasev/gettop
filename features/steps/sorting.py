from behave import given, when, then


@when('Sort products on macbook Category page by price: high to low')
def sort_by_price_high_to_low(context):
    context.app.sorting.sort_by_price_high_to_low()


@when('Sort products on macbook Category page by price: low to high')
def sort_by_price_low_to_high(context):
    context.app.sorting.sort_by_price_low_to_high()


@when('Sort products on  macbook Category page by popularity')
def sort_by_popularity(context):
    context.app.sorting.sort_by_popularity()


@when('Sort products on macbook Category page by rating')
def sort_by_rating(context):
    context.app.sorting.sort_by_rating()


@when('Sort products on macbook Category page by latest')
def sort_by_latest(context):
    context.app.sorting.sort_by_latest()


@then('Verify products sorted by price: high to low')
def verify_sorted_by_price_high_to_low(context):
    context.app.sorting.verify_sorted_by_price_high_to_low()


@then('Verify products sorted by price: low to high')
def verify_sorted_by_price_low_to_high(context):
    context.app.sorting.verify_sorted_by_price_low_to_high()


@then('Verify products on macbook Category page sorted by popularity')
def verify_sorted_by_popularity(context):
    context.app.sorting.verify_sorted_by_popularity()


@then('Verify products on macbook Category page sorted by rating')
def verify_sorted_by_rating(context):
    context.app.sorting.verify_sorted_by_rating()


@then('Verify products on macbook Category page sorted by latest')
def verify_sorted_by_latest(context):
    context.app.sorting.verify_sorted_by_latest()