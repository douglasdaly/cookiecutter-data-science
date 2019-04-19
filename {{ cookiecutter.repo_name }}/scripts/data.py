#!/usr/bin/env {{ cookiecutter.python_interpreter }}
# -*- coding: utf-8 -*-
"""
Script tools for getting and processing the project's data.
"""
#
#   Imports
#
import os
import logging

import click
import dotenv


#
#   Globals
#

PROJECT_DIR = None
DATA_DIR = None
RAW_DIR = None
PROCESSED_DIR = None
INTERIM_DIR = None
COOKED_DIR = None


#
#   Setup
#

logger = logging.getLogger(__name__)
dotenv.load_dotenv()


#
#   Script commands
#

@click.group()
@click.pass_context
def cli(ctx):
    """
    Tools for acquiring and processing data.
    """
    ctx.ensure_object(dict)


@cli.command()
@click.pass_context
def get(ctx):
    """
    Tool for acquiring the raw data files.
    """
    # [START] Data acquisition code here
    pass


@cli.command()
@click.pass_context
def process(ctx):
    """
    Tool for processing the raw data files.
    """
    # [START] Data processing code here
    pass


@cli.command()
@click.pass_context
def cook(ctx):
    """
    Tool for cooking the processed data files.
    """
    # [START] Data cooking code here
    pass


#
#   Entry-point
#

if __name__ == "__main__":
    # - Configure logging
    log_fmt = '[%(levelname)s %(name)s %(asctime)s] %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # - Relevant paths
    PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.pardir)
    DATA_DIR = os.path.join(PROJECT_DIR, 'data')
    RAW_DIR = os.path.join(DATA_DIR, 'raw')
    PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')
    INTERIM_DIR = os.path.join(DATA_DIR, 'interim')
    COOKED_DIR = os.path.join(DATA_DIR, 'cooked')

    # - Run Main Function
    cli(obj={})
