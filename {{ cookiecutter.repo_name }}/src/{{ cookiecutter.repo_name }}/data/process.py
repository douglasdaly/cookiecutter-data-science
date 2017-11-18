# -*- coding: utf-8 -*-
"""
process.py

    Modules for processing the raw data

@author: Douglas Daly
@date: 11/18/2017
"""
#
#   Imports
#
import pandas as pd
import numpy as np


#
#   Function Definitions
#

def split_x_y_dataframe(data, y_columns, x_columns=None):
    """ Splits DataFrame into X and Y DataFrames

    :param pandas.DataFrame data: Data to split
    :param list y_columns: Y Data column(s) to grab
    :param list x_columns: X Data columns to grab

    :return: DataFrames for X and Y data
    :rtype: tuple

    """
    if type(y_columns) == str:
        y_columns = [y_columns]

    if set(y_columns).issubset(data.columns):
        y_data = data[y_columns]
    else:
        y_data = None

    if x_columns is not None:
        if type(x_columns) == str:
            x_columns = [x_columns]

        x_data = data[x_columns]
    else:
        if y_data is not None:
            x_data = data.drop(y_columns, axis=1)
        else:
            x_data = data.copy()

    return x_data, y_data


def one_hot_text_dataframe_columns(data, columns):
    """ One-Hot's Text Columns

    :param pandas.DataFrame data: DataFrame to use
    :param list columns: Columns of Text data to one-hot

    :return: New DataFrame with the One-Hotted columns
    :rtype: pandas.DataFrame

    """
    if type(columns) == str:
        columns = [columns]

    return pd.get_dummies(data, columns=columns, prefix=columns)


def get_text_column_names(data, ignore_columns=None):
    """ Gets names of Columns in DataFrame containing text

    :param data: DataFrame to get text column names from
    :param ignore_columns: Columns to ignore

    :return: List of columns containing text data
    :rtype: list

    """
    if ignore_columns is not None:
        cols_2_check = data.columns - ignore_columns
    else:
        cols_2_check = data.columns

    temp = data[cols_2_check]
    test = temp.applymap(type).eq(str).any()
    test = test[test == True]

    return list(test.index.values)
