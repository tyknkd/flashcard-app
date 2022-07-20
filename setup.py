#!/usr/bin/python3

# Python script describing project for installation
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/install/

from setuptools import find_packages, setup

setup(
    name='wordsalad',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
