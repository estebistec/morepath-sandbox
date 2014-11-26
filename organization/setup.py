#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup for organization
"""


from setuptools import find_packages
from setuptools import setup


setup(
    name='organization',
    version='0.1.0',
    description='Simple morepath project',
    # long_description='',
    author='Steven Cummings',
    author_email='cummingscs@gmail.com',
    url='https://github.com/estebistec/organization',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['organization'],
    include_package_data=True,
    install_requires=[
        'morepath==0.9',
        'Werkzeug==0.9.6'
    ],
    license="BSD",
    zip_safe=False,
    keywords='organization',
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
    tests_require=[],
    entry_points={
        'console_scripts': [
            'organization-start = organization.main:main'
        ]
    }
)
