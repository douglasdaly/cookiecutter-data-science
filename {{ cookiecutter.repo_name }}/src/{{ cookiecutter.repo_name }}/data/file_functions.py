# -*- coding: utf-8 -*-
"""
file_functions.py

    Functions for working with data files

@author: Douglas Daly
@date: 11/18/2017
"""
#
#   Imports
#
import os
import pickle


#
#   Function Definitions
#

def save_data_as_pickle(data, filename, overwrite=False):
    """ Saves the given Data as a Pickle file

    :param object data: Data object to save
    :param str filename: File to save to
    :param bool overwrite: [Optional] Overwrite existing? (Default is False)

    :return: Success/failure of the Save
    :rtype: bool

    """
    if os.path.exists(filename) and not overwrite:
        return False

    with open(filename, 'wb') as fout:
        pickle.dump(data, fout)

    return True


def load_data_from_pickle(filename):
    """ Loads data from a Pickled file

    :param str filename: File to load

    :return: Data requested from pickled file (None on error)
    :rtype: object

    """
    if not os.path.exists(filename):
        return None

    with open(filename, 'rb') as fin:
        ret = pickle.load(fin)

    return ret
