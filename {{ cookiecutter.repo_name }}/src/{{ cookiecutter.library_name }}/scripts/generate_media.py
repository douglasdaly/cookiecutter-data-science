#!/usr/bin/env {{ cookiecutter.python_interpreter }}
# -*- coding: utf-8 -*-
"""
scripts/generate_media.py

    Script for generating media files related to the project.

"""
#
#   Imports
#
import click


#
#   Script Functions
#

@click.group()
@click.pass_context
def cli(ctx):
    """Tools for generating media files"""
    ctx.ensure_object(dict)


#
#   Entry-point
#

if __name__ == "__main__":
    cli(obj={})
