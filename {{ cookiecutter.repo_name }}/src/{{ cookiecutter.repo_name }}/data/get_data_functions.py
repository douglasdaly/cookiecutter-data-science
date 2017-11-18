# -*- coding: utf-8 -*-
"""
get_data_functions.py

    Functions to facilitate data getting.

@author: Douglas Daly
@date: 11/17/2017
"""
#
#   Imports
#
import requests

from tqdm import tqdm


#
#   Function Definitions
#

def download_file(url, filename, show_status=True, desc=''):
    """ Downloads a file from the internet

    Downloads the target file from the given url and saves it locally to the
    given filename.  Optionally shows the download status as it progresses.

    Parameters
    ----------
    url: str
        URL to download the file from
    filename: str
        File to save the file to

    show_status: bool, optional
        Whether or not to show a progress bar as the file is downloaded
    desc: str, optional
        Description to display in the progress bar

    Returns
    -------
    bool
        The result status of the download and save

    """
    r = requests.get(url, stream=True)

    total_size = int(r.headers.get('content-length', 0))
    with open(filename, 'wb') as fout:
        if show_status:
            for f_chunk in tqdm(r.iter_content(32*1024), total=total_size,
                                unit='B', unit_scale=True, desc=desc):
                fout.write(f_chunk)
        else:
            for f_chunk in r.iter_content(32*1024):
                fout.write(f_chunk)

    return True
