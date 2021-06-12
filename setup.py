#!/usr/bin/env python
"""Setup script for the project."""

from __future__ import print_function

import codecs
import os

from setuptools import setup

IMPORT = 'sphinxcontrib.disqus'
INSTALL_REQUIRES = ['sphinx-disqus']
LICENSE = 'MIT'
NAME = 'sphinxcontrib-disqus'
VERSION = '1.1.1'


def readme(path='README.rst'):
    """Try to read README.rst or return empty string if failed.

    :param str path: Path to README file.

    :return: File contents.
    :rtype: str
    """
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), path))
    handle = None
    url_prefix = 'https://raw.githubusercontent.com/Robpol86/{name}/v{version}/'.format(name=NAME, version=VERSION)
    try:
        handle = codecs.open(path, encoding='utf-8')
        return handle.read(131072).replace('.. image:: docs', '.. image:: {0}docs'.format(url_prefix))
    except IOError:
        return ''
    finally:
        getattr(handle, 'close', lambda: None)()


setup(
    author='@Robpol86',
    author_email='robpol86@gmail.com',
    classifiers=[
        'Development Status :: 7 - Inactive',
    ],
    description='Sphinx extension that embeds Disqus comments in documents.',
    install_requires=INSTALL_REQUIRES,
    keywords='sphinx disqus',
    license=LICENSE,
    long_description=readme(),
    name=NAME,
    packages=['sphinxcontrib'],
    url='https://pypi.org/project/sphinxcontrib-disqus/',
    version=VERSION,
    zip_safe=False,
)
