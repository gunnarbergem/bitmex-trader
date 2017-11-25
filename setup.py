#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import dirname, join, isfile

here = dirname(__file__)

setup(name='bitmex-trader',
      version='0.1',
      description='Order executor for BitMEX API',
      long_description=open(join(here, 'README.md')).read(),
      url='',
      install_requires=[
          'requests',
          'websocket-client',
          'future'
      ]
      )
