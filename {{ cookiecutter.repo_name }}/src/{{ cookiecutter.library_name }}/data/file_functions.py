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
from abc import ABCMeta


#
#   Function Definitions
#

def save_to_pickle(data, filename, overwrite=False):
    """Saves the given Data as a Pickle file

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

    Raises
    ------
    FileAlreadyExistsError
        If the specified file already exists and the `overwrite` parameter
        is not set.

    Returns
    -------
    bool
        Result status of the save operation

    See Also
    --------
    load_data_from_pickle

    """
    if not overwrite:
        check_file_exists(filename)

    with open(filename, 'wb') as fout:
        pickle.dump(data, fout)

    return True


def load_from_pickle(filename):
    """ Loads data from a Pickled file

    Loads an object saved via pickle to the given filename.

    Parameters
    ----------
    filename: str
        File to load the pickled object from.

    Raises
    ------
    FileDoesNotExistError
        If the specified `filename` does not exist.

    Returns
    -------
    object
        Object saved in the pickled file.

    See Also
    --------
    save_to_pickle

    """
    check_file_exists(filename)

    with open(filename, 'rb') as fin:
        ret = pickle.load(fin)

    return ret


#
#   Helper Functions
#

def check_file_exists(filename, raise_exception=True):
    """Checks if the given filename exists or not

    Parameters
    ----------
    filename: str
        File to check existence of.

    raise_exception: bool, optional
        Whether or not to raise an exception if the file doesn't exist.

    Raises
    ------
    FileDoesNotExistError
        If the specified file doesn't exist.

    Returns
    -------
    bool
        Whether or not the specified file exists.

    """
    if not os.path.exists(filename):
        if raise_exception:
            raise FileDoesNotExistError(filename)


#
#   Exception Classes
#

class BaseFileException(Exception, metaclass=ABCMeta):
    """
    Base Class for File Exceptions

    Attributes
    ----------
    filename: str
        Filename related to this exception.

    """
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        """str: Filename for this exception"""
        return self._filename


class FileAlreadyExistsError(BaseFileException):
    """
    File Already Exists Exception Class
    """

    def __str__(self):
        return "The specified file already exists: {}".format(self._filename)


class FileDoesNotExistError(BaseFileException):
    """
    File Does Not Exist Exception Class
    """

    def __str__(self):
        return "The specified file does not exist: {}".format(self._filename)
