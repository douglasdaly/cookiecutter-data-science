# -*- coding: utf-8 -*-
"""
data Module

    Functions and classes to help with acquiring and processing data.

@author: Douglas Daly
@date: 12/11/2018
"""
#
#   Imports
#
from . import web
from .dataframe_helpers import (df_get_text_column_names,
                                df_one_hot_text_columns, df_split_columns)
from .file_functions import (save_to_pickle, load_from_pickle,
                             check_file_exists)


#
#   All Setup
#
__all__ = [
    # Modules
    'web',
    # Functions
    # - Pandas
    'df_one_hot_text_columns',
    'df_split_columns',
    'df_get_text_column_names',
    # - File
    'save_to_pickle',
    'load_from_pickle',
    'check_file_exists',
]
