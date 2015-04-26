__author__ = 'Matthew'

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='bbmove',
    version='0.1',
    packages=['bbmove'],
    url='',
    license='MIT',
    author='Matthew Kendon',
    author_email='mkendon@gmail.com',
    description='Import tvshows from download to folder on computer with filename change',
    long_description=readme(),
    tests_require=['behave']
)
