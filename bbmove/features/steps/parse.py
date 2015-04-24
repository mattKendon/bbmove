__author__ = 'Matthew'

from behave import *
from bbmove import search, Video

@when('I parse the files')
def step_impl(context):
    context.search_result = [Video(file) for file in search(context.test_dir)]

@then('I should see the title "{title}"')
def step_impl(context, title):
    assert title in [file.title for file in context.search_result]