# -*- coding: utf-8 -*-
"""
parse.py

    Module for parsing data

@author: Douglas Daly
@date: 11/18/2017
"""
#
#   Imports
#
import pandas as pd


#
#   Function Definitions
#

def parse_csv_as_dataframe(filename, index=None):
    """ Parses a CSV file into a DataFrame

    Parses the contents of the given CSV file into a pandas DataFrame

    Parameters
    ----------
    filename: str
        CSV file to load data from

    index: str, optional
        Column name to set as the DataFrame's index

    Returns
    -------
    pandas.DataFrame
        DataFrame of the file data requested

    """
    df_data = pd.read_csv(filename)
    if index is not None:
        df_data.set_index(index, inplace=True)
    return df_data
