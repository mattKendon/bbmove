__author__ = 'Matthew'

import shutil
import os


def before_all(context):
    context.test_dir = "test"
    context.tv_show_dir = "test_tv"


def after_scenario(context, scenario):
    if os.path.exists(context.test_dir):
        shutil.rmtree(context.test_dir)
    if os.path.exists(context.tv_show_dir):
        shutil.rmtree(context.tv_show_dir)