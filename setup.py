#!/usr/bin/python3

# -*- coding: utf-8 -*-

import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(name='multipass-compose',
    version='0.1',
    description='A python wrapper for multipass',
    long_description=long_description,
    long_description_content_type="text/markdown",      
    url='https://github.com/jumidev/multipass-compose',
    author='krezreb',
    author_email='josephbeeson@gmail.com',
    license='MIT',
    packages=["."],
    zip_safe=False,
    install_requires=[
        'pyyml'
    ],
    entry_points = {
              'console_scripts': [
                  'multipass-compose=multipass_compose:main'              ],              
          },

    )





