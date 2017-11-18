# -*- coding: utf-8 -*-
"""
process_data.py

    Script to process the raw data and store a more usable version

@author: Douglas Daly
@date: 11/18/2017
"""
#
#   Imports
#
import os
import click
import logging


#
#   Variable Definitions
#

PROJECT_DIR = None

DATA_DIR = None
__DATA_DIR_NAME = 'data/'

RAW_DIR = None
___RAW_DATA_DIR_NAME = 'raw/'

PROCESSED_DIR = None
__PROCESSED_DATA_DIR_NAME = 'processed/'


#
#   Function Definitions
#


#
#   Main Script
#

@click.command()
def main():
    """ Main Script Function
    """
    # - Logger
    logger = logging.getLogger(__name__)

    # [Start] DATA PROCESSING CODE

    # - Get the Data
    logger.info("Loading in raw data...")

    # - Process the Data
    logger.info("Processing raw data...")

    # - Save the Processed Data
    logger.info("Saving processed data...")

    # [ End ] DATA PROCESSING CODE

    logger.info("Data processing complete.")


if __name__ == "__main__":
    # - Setup Logging
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # - Setup Variables
    PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.pardir)
    DATA_DIR = os.path.join(PROJECT_DIR, __DATA_DIR_NAME)
    RAW_DIR = os.path.join(DATA_DIR, ___RAW_DATA_DIR_NAME)
    PROCESSED_DIR = os.path.join(DATA_DIR, __PROCESSED_DATA_DIR_NAME)

    # - Run Main Function
    main()
