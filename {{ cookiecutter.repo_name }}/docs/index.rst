.. {{ cookiecutter.project_name }} documentation master file, created by
   sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{% for _ in cookiecutter.project_name %}#{% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}#{% endfor %}

*{{ cookiecutter.description }}*


Contents:

.. toctree::
   :maxdepth: 2

   getting-started
   commands



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
