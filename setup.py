#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as file_readme:
    readme = file_readme.read()

setup(name='json-sempai',
      version='0.3.1',
      description='Use JSON files as if they\'re python modules',
      long_description=readme,
      author='Louis Taylor',
      author_email='kragniz@gmail.com',
      license='MIT',
      url='https://github.com/kragniz/json-sempai',
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
      keywords='please don\'t use this library for anything',
      packages=['jsonsempai', 'jsonsempai.tests'],
      test_suite='jsonsempai.tests'
)
