#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup for quickstart
"""


from setuptools import find_packages
from setuptools import setup


setup(
    name='quickstart',
    version='0.1.0',
    description='Simple morepath project',
    # long_description='',
    author='Steven Cummings',
    author_email='cummingscs@gmail.com',
    url='https://github.com/estebistec/quickstart',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['quickstart'],
    include_package_data=True,
    install_requires=[
        'morepath==0.9'
    ],
    license="BSD",
    zip_safe=False,
    keywords='quickstart',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=[]
)
