#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('AUTHORS.rst') as authors_file:
    authors = authors_file.read()

requirements = ['dicttoxml', 'PyYAML']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="LaserPhaser",
    author_email='arseny.antonov@gmail.com',
    classifiers=[
        'Framework :: Pytest',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Formatter for pytest collect output",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history + '\n\n' + authors,
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'yaml', 'json'
    ],
    name='pytest-collect-formatter',
    packages=find_packages(include=['pytest_collect_formatter']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/LaserPhaser/pytest-collect-formatter',
    version='0.1.0',
    zip_safe=False,
    entry_points={
        'pytest11': [
            'pytest-collect-formatter = pytest_collect_formatter.plugin',
        ]
    }
)
