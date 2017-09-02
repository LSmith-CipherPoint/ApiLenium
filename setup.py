#!/usr/bin/env python
# coding=utf-8
"""
Setup.py for ApiLenium
"""

from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_dsecription = f.read()

config = {
    'url': 'https://github.com/LSmith-CipherPoint/ApiLenium',
    'name': 'ApiLenium',
    'version': '0.0.1',
    'description': 'Selenium API Testing',
    'long_description': long_dsecription,
    'author': 'Luke Smith',
    'author_email': 'lsmith@cipherpoint.com',
    'license': 'BSD',
    'entry_points': {
        'console_scripts': [
            'apilenium = ApiLenium.__main__:main'
        ]
    },
    'packages': find_packages(exclude=[
        "tests",
        "tests.*",
        "*.tests",
        "*.tests.*"
    ]),
    'install_requires': [
        'selenium'
    ],
    'tests_require': [
        'pytest',
        'nose'
    ],
    'extras_require': {
        'test': [
            'pytest'
        ],
        'docstest': [
            'doc8',
            'pyenchant',
            'readme_renderer >= 16.0',
            'sphinx',
            'sphinx_rtd_theme',
            'sphinxcontrib-spelling'
        ],
        'pep8test': [
            'flake8',
            'flake8-import-order',
            'pep8-naming'
        ]
    }
}

setup(**config)
