__author__ = 'Matthew'

from behave import *
from bbmove import move, touch, Video
import os


@when('I move the files')
def step_impl(context):
    move(context.test_dir, context.tv_show_dir)


@then('I must see "{filename}" in the tv show folder')
def step_impl(context, filename):
    file = Video(filename)
    os.path.exists(os.path.join("test_tv", file.folder_tree, filename))