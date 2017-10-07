# -*- coding: utf-8 -*-

#
#   Imports
#
from distutils.core import setup

#
#   Setup Code
#

setup(name="{{ cookiecutter.project_name }} dataproj Library",
      version="0.1dev",
      packages=['dataproj', ],
      package_dirs={'dataproj': 'src'},
      license="MIT",
      long_description=open("README.md").read()
      )
