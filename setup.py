#!/usr/bin/env python3
'''
Hoot Interactive - DBBackup
'''

import os
from setuptools import setup


setup(
    name='Hoot Interactive - DBBackup',
    version='0.1',
    author='Estevo Paz',
    author_email='estevo@hootinteractive.net',
    description='Easy remote database backup system',
    packages=[],
    scripts=['bin/' + script for script in os.listdir('bin')],
    keywords='python3',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3',
        'Topic :: Python',
    ]
)
