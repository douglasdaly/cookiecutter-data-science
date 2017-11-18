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

    :param str filename: File to parse
    :param str index: [Optional] Column to set as index (Default is None)

    :return: DataFrame representation of the file data
    :rtype: pandas.DataFrame

    """
    df_data = pd.read_csv(filename)
    if index is not None:
        df_data.set_index(index, inplace=True)
    return df_data
