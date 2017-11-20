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

    Given a DataFrame and Y column(s), split the DataFrame into two seperate
    DataFrames, one with the X data and one with the Y data based on the
    parameters given.  If the given data doesn't contain the `y_columns` then
    `None` is returned (e.g. the testing data).

    Parameters
    ----------
    data: pandas.DataFrame
        Data to split into seperate X and Y DataFrames
    y_columns: str or list of strings
        Column(s) which represent the Y data to split out

    x_columns: str or list of strings, optional
        Specific column(s) to use as the X data to split out

    Returns
    -------
    pandas.DataFrame
        The X data split out from the given `data`
    pandas.DataFrame
        The Y data split out from the given `data`

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

    Given a DataFrame (`data`) replace the given `columns` with new ones
    representing a one-hot on each of the given `columns` using the original
    column name followed by an underscore as the new columns prefix.

    Parameters
    ----------
    data: pandas.DataFrame
        Data to run one-hot conversions over
    columns: str or list of strings
        Column(s) to replace with one-hotted values

    Returns
    -------
    pandas.DataFrame
        DataFrame with the `columns` values replaced with one-hotted values

    See Also
    --------
    get_text_column_names

    """
    if type(columns) == str:
        columns = [columns]

    return pd.get_dummies(data, columns=columns, prefix=columns)


def get_text_column_names(data, ignore_columns=None):
    """ Gets names of Columns in DataFrame containing text data

    Returns a list of all the columns in the given `data` which have any string
    data in them (not necessarily all string data - if the column contains a
    single `str` it will be included in the return list).

    Parameters
    ----------
    data: pandas.DataFrame
        Data to check each column for string data in

    ignore_columns: list
        List of columns to ignore in the checking process

    Returns
    -------
    list
        List of the column names which contain string data

    """
    if ignore_columns is not None:
        cols_2_check = data.columns - ignore_columns
    else:
        cols_2_check = data.columns

    temp = data[cols_2_check]
    test = temp.applymap(type).eq(str).any()
    test = test[test is True]

    return list(test.index.values)
