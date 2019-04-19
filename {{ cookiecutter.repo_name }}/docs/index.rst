.. {{ cookiecutter.project_name }} documentation master file, created by
   sphinx-quickstart on Sun Mar 31 16:33:43 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{ cookiecutter.project_name }}'s documentation!
==========={% for _ in cookiecutter.project_name %}={% endfor %}=================

**{{ cookiecutter.description }}**


.. toctree::
    :maxdepth: 2
    :caption: Getting Started:

    getting-started
    commands


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
