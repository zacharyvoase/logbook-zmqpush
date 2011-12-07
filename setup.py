#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
import os.path as p

VERSION = open(p.join(p.dirname(p.abspath(__file__)), 'VERSION')).read().strip()

setup(
    name='logbook-zmqpush',
    version=VERSION,
    description='ZMQ_PUSH-based handler for Logbook',
    author='Zachary Voase',
    author_email='z@zacharyvoase.com',
    url='http://github.com/zacharyvoase/logbook-zmqpush',
    py_modules=['logbook_zmqpush'],
    package_dir={'': 'lib'},
    install_requires=[
        'Logbook==0.3',
        'pyzmq==2.1.10',
    ],
)
