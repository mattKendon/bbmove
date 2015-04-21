__author__ = 'Matthew'

from behave import *
from bbmove import search
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
    assert filename in context.search_result


@then('I must not see "{filename}"')
def step_impl(context, filename):
    assert filename not in context.search_result


def touch(path):
    basedir = os.path.dirname(path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    with open(path, 'a'):
        os.utime(path, None)