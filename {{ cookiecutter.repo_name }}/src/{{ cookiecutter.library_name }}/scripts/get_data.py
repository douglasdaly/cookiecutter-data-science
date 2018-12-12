#!/usr/bin/env {{ cookiecutter.python_interpreter }}
# -*- coding: utf-8 -*-
"""
scripts/get_data.py

    Script which acquires the raw data set and saves it.

"""
#
#   Imports
#
import os
import click
import logging
from dotenv import find_dotenv, load_dotenv


#
#   Variable Definitions
#

DATA_DIR_LOC = 'data/raw/'

PROJECT_DIR = None
DATA_DIR = None


#
#   Script Functions
#

@click.group()
@click.pass_context
def cli(ctx):
    """Downloads and saves raw data for this project"""
    logger = logging.getLogger(__name__)
    logger.info("Starting data acquisition...")

    # [Start] CODE TO ACQUIRE AND SAVE DATA

    # [ End ] CODE TO ACQUIRE AND SAVE DATA

    logger.info("Finished data acquisition.")


#
#   Script Entry-point
#

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    DATA_DIR = os.path.join(PROJECT_DIR, DATA_DIR_LOC)

    # find .env automatically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    cli(obj={})
