from behave import given, then, when


@then('Verify Description block is shown')
def verify_description(context):
    context.app.des.verify_description()