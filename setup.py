#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Batman',
    version='0.6.0',
    description='A deployment toolbelt',
    author='Kevin McCarthy',
    author_email='me@kevinmccarthy.org',
    url='https://github.com/realgeeks/batman',
    packages=find_packages(),
    license='MIT',
    install_requires=['PyYAML==3.10', 'argparse==1.2.1', 'virtualenvwrapper==4.0'],
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
