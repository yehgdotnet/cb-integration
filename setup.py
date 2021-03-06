#!/usr/bin/env python

import sys

sys.path.insert(0, "src/")

# TODO: fix version handling...
version="5.1.0.15137"

from setuptools import setup

setup(
    name='python-cb-integration',
    version=version,
    url='http://www.bit9.com/',
    license='MIT',
    author='Carbon Black',
    author_email='dev-support@bit9.com',
    description='Carbon Black Integration Library',
    long_description=__doc__,
    packages=['cbint', 'cbint.utils', 'cbint.utils.detonation'],
    package_data={'cbint': ['utils/templates/*'], 'cbint.utils.detonation': ['templates/*']},
    package_dir = {'': 'src'},
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['flask', 'python-dateutil', 'netifaces']
)
