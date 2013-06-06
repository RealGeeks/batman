#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

install_requires = ['PyYAML==3.10', 'virtualenvwrapper==4.0']

if sys.version_info < (2, 7):
    install_requires += ['ordereddict==1.1', 'argparse==1.2.1']

setup(
    name='Batman',
    version='0.6.0',
    description='A deployment toolbelt',
    author='Kevin McCarthy',
    author_email='me@kevinmccarthy.org',
    url='https://github.com/realgeeks/batman',
    packages=find_packages(),
    license='MIT',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'batman = batman.main:batmain',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: System :: Installation/Setup',
        'Topic :: Software Development :: Version Control',
        'License :: OSI Approved :: MIT License',
    ],
)


