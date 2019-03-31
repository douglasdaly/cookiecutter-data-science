########
Commands
########

The ``Makefile`` contains the recipes for common tasks related to this project.


Syncing data to S3
==================

The following are used for working with S3 buckets:

sync_data_to_s3
    Will use ``aws s3 sync`` to recursively sync files in ``data/`` up to
    ``s3://{{ cookiecutter.s3_bucket }}/data/``.

sync_data_from_s3
    Will use ``aws s3 sync`` to recursively sync files from
    ``s3://{{ cookiecutter.s3_bucket }}/data/`` to ``data/``.
