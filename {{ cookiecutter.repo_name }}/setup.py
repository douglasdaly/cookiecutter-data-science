# -*- coding: utf-8 -*-
"""
setup.py

      Setup file for installing this project's library.

@author: Douglas Daly
@date: 12/11/2018
"""
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
      version="0.0.1",
      author="{{ cookiecutter.author_name }}",
      license="{{ cookiecutter.open_source_license }}",
      long_description=open("README.md").read(),

      packages=find_packages('src'),
      package_dirs={'': 'src'},

      entry_points={
            'console_scripts': [
                  'build_features={{ cookiecutter.library_name }}.scripts.build_features:cli',
                  'generate_media={{ cookiecutter.library_name }}.scripts.generate_media:cli',
                  'get_data={{ cookiecutter.library_name }}.scripts.get_data:cli',
                  'process_data={{ cookiecutter.library_name }}.scripts.process_data:cli',
            ],
      },
)
