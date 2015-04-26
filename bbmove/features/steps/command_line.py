__author__ = 'Matthew'


from behave import *
from click.testing import CliRunner
from bbmove import cli


@when('I run the search command')
def step_impl(context):
    context.runner = CliRunner()
    context.search_results = context.runner.invoke(cli.cli, ['search', context.test_dir])


@when('I run the move command')
def step_impl(context):
    context.runner = CliRunner()
    context.search_results = context.runner.invoke(cli.cli, ['move', context.test_dir, context.tv_show_dir])


@then('I must find "{filename}" in the results')
def step_impl(context, filename):
    assert context.search_results.exit_code == 0
    assert filename in context.search_results.output