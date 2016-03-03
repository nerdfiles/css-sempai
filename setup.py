#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as file_readme:
    readme = file_readme.read()

setup(name='css-sempai',
      version='0.4.0',
      description='Use CSS files as if they\'re python modules',
      long_description=readme,
      author='nerdfiles',
      author_email='nerdfiles@gmail.com',
      license='WTFPL',
      url='https://github.com/nerdfiles/css-sempai',
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
      packages=['csssempai', 'csssempai.tests'],
      test_suite='csssempai.tests'
)

