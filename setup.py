#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

setup(
    name='Batman',
    version='0.1',
    description='A deployment toolbelt',
    author='Kevin McCarthy',
    author_email='me@kevinmccarthy.org',
    url='http://kevinmccarthy.org',
    packages=find_packages(),
    install_requires=['PyYAML>=3.10','argparse>=1.1'],
    entry_points={
        'console_scripts': [
            'batman = batman.main:main',
        ]
    },
)

