__author__ = 'Matthew'

from behave import *
from bbmove import search, touch
import os

@given('there are some files')
def step_impl(context):
    for row in context.table:
        filename = context.test_dir + os.sep + row['filename']
        touch(filename)


@when('I search for files')
def step_impl(context):
    context.search_result = search(context.test_dir)


@then('I must see "{filename}"')
def step_impl(context, filename):
    assert len([filepath for filepath in context.search_result if filename in filepath]) == 1


@then('I must not see "{filename}"')
def step_impl(context, filename):
    assert len([filepath for filepath in context.search_result if filename in filepath]) == 0