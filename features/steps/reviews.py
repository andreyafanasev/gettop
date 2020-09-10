from behave import when, then


@when('Click review top link')
def click_review_top(context):
    context.app.review.click_review_top()


@when('Click 5-star review link')
def click_5_star(context):
    context.app.review.click_5_star()


@when('Fill out review form (review, name, email)')
def fill_out_review_form(context):
    context.app.review.fill_out_review_form()


@when('Click SUBMIT button')
def click_submit(context):
    context.app.review.click_submit()


@then('Verify review is shown')
def verify_review(context):
    context.app.review.verify_review()


@then('Verify correct amount of product (MacBook Air) reviews are shown')
def verify_amount_reviews_macbook_air(context):
    context.app.review.verify_amount_reviews_macbook_air()