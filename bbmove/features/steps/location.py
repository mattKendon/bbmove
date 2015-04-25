import os

__author__ = 'Matthew'

from behave import *


@then('I must see the tv show folder name "{folder}"')
def step_impl(context, folder):
    assert folder in [file.title_folder for file in context.search_result]

@then('I must see the season folder name "{folder}"')
def step_impl(context, folder):
    assert folder in [file.season_folder for file in context.search_result]

@then('I must see the folder tree "{tv_show}/{season}"')
def step_impl(context, tv_show, season):
    assert os.path.join(tv_show, season) in [file.folder_tree for file in context.search_result]