#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

setup(
    name='Batman',
    version='0.2',
    description='A deployment toolbelt',
    author='Kevin McCarthy',
    author_email='me@kevinmccarthy.org',
    url='https://github.com/realgeeks/batman',
    packages=find_packages(),
    license='MIT',
    install_requires=['PyYAML>=3.10', 'argparse>=1.1'],
    entry_points={
        'console_scripts': [
            'batman = batman.main:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: System :: Installation/Setup',
        'Topic :: Software Development :: Version Control',
        'License :: OSI Approved :: MIT License',
    ],
)
