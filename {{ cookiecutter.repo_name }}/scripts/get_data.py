# -*- coding: utf-8 -*-
"""
get_data.py

    Script which acquires the raw data set and saves it.

@author: Douglas Daly
@date: 11/18/2017
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
#   Function Definitions
#


#
#   Main Script
#


@click.command()
def main():
    """ Downloads and saves raw data for this project into the DATA_DIR
    """
    logger = logging.getLogger(__name__)
    logger.info("Starting data acquisition...")

    # [Start] CODE TO ACQUIRE AND SAVE DATA

    # [ End ] CODE TO ACQUIRE AND SAVE DATA

    logger.info("Finished data acquisition.")


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    DATA_DIR = os.path.join(PROJECT_DIR, DATA_DIR_LOC)

    # find .env automatically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
