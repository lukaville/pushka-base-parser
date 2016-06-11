#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os
import re

from setuptools import setup


def get_version_from_init():
    file = open(os.path.join(os.path.dirname(__file__), 'pushka_base_parser', '__init__.py'))

    regexp = re.compile(r".*__version__ = '(.*?)'", re.S)
    version = regexp.match(file.read()).group(1)
    file.close()

    return version


setup(
    name='pushka_base_parser',
    license='MIT',
    author='Nickolay Chameev',
    author_email='nickolay@chameev.ru',
    version=get_version_from_init(),
    url='https://github.com/lukaville/pushka-base-parser',
    packages=[
        'pushka_base_parser',
        'pushka_base_parser.store',
        'pushka_base_parser.test'
    ],
    package_dir={
        'pushka_base_parser': 'pushka_base_parser',
        'pushka_base_parser.store': 'pushka_base_parser/store',
    },
    install_requires=[
        'pymongo==3.2.1', 'rabbit_bind==1.0.1', 'rabbit_rpc==0.12345'
    ],
    dependency_links=[
        'git+https://github.com/dimorinny/rabbit-bind.git#egg=rabbit_bind-1.0.1',
        'git+https://github.com/iskandarov-egor/rabbit-rpc.git#egg=rabbit_rpc-0.12345'
    ]
)
