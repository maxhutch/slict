#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import slict

setup(name='slict',
      version=slict.__version__,
      description='Sliceable dictionary',
      url='http://github.com/maxhutch/slict/',
      author='https://raw.github.com/maxhutch/slict/master/AUTHORS.md',
      author_email='maxhutch@gmail.com',
      maintainer='Max Hutchinson',
      maintainer_email='maxhutch@gmail.com',
      license='BSD',
      keywords='dictionary slice',
      packages=['slict'],
      zip_safe=True)
