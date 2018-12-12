#!/usr/bin/env {{ cookiecutter.python_interpreter }}
# -*- coding: utf-8 -*-
"""
scripts/build_features.py

    This script is responsible for taking the pre-processed data and creating
    feature data from it.

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
    """Tools for generating feature data"""
    ctx.ensure_object(dict)


#
#   Main Entry Point
#

if __name__ == "__main__":
    cli(obj={})
