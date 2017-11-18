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

def save_data_to_pickle(data, filename, overwrite=False):
    """ Saves the given Data as a Pickle file

    Saves the given data object, whatever it may be (but must be a pickle-able
    object) to the given filename with the optional ability to overwrite an
    existing file.

    Parameters
    ----------
    data: object
        Data to save to the pickle file
    filename: str
        File to save the object to

    overwrite: bool, optional
        Whether or not to overwrite the file if it already exists

    Returns
    -------
    bool
        Result status of the save operation

    See Also
    --------
    load_data_from_pickle

    """
    if os.path.exists(filename) and not overwrite:
        return False

    with open(filename, 'wb') as fout:
        pickle.dump(data, fout)

    return True


def load_data_from_pickle(filename):
    """ Loads data from a Pickled file

    Loads an object saved via pickle to the given filename.

    Parameters
    ----------
    filename: str
        File to load the pickled object from

    Returns
    -------
    object
        Object saved in the pickled file

    See Also
    --------
    save_data_to_pickle

    """
    if not os.path.exists(filename):
        return None

    with open(filename, 'rb') as fin:
        ret = pickle.load(fin)

    return ret
