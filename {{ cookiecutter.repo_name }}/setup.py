# -*- coding: utf-8 -*-

#
#   Imports
#
from distutils.core import setup
from setuptools import find_packages

#
#   Setup Code
#

setup(
      name="{{ cookiecutter.project_name }} Project Library",
      version="0.1",
      author="{{ cookiecutter.author_name }}",
      packages=find_packages('src'),
      package_dirs={'': 'src'},
      license="{{ cookiecutter.open_source_license }}",
      long_description=open("README.md").read()
)
