#! /usr/bin/env python

from distutils.core import setup
from ov6 import __version__


setup(name='ov6',
      version=__version__,
      description='Python wrapper for Ovh api v6',
      author='Guillaume Dugas',
      author_email='dugas.guillaume@gmail.com',
      url='https://github.com/gdugas/ov6',
      py_modules=['ov6'],
      classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
      ]
     )
