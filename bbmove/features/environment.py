__author__ = 'Matthew'

from behave import *
import shutil


def before_all(context):
    context.test_dir = "test"


def after_scenario(context, scenario):
    shutil.rmtree(context.test_dir)
