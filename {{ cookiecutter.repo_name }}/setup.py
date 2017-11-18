# -*- coding: utf-8 -*-

#
#   Imports
#
from distutils.core import setup

#
#   Setup Code
#

setup(name="{{ cookiecutter.project_name }} Project Library",
      version="0.1dev",
      packages=['{{ cookiecutter.repo_name }}'],
      package_dirs={'': 'src'},
      license="MIT",
      long_description=open("README.md").read()
)
