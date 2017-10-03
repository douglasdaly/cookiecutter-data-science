# -*- coding: utf-8 -*-
"""
make_dataset.py

    Script which acquires the data set and pre-processes it for exploration and feature engineering.

@author: Douglas Daly
@date: 10/2/2017
"""
#
#   Imports
#
import os
import click
import logging
from dotenv import find_dotenv, load_dotenv

#
#   Function Definitions
#

@click.command()
def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)

    # CODE TO ACQUIRE DATA

#
#   Script Entry-Point
#
if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automatically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
