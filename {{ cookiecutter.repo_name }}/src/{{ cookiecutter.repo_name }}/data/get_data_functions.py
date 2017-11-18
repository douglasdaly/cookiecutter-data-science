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
import logging

from tqdm import tqdm


#
#   Function Definitions
#

def download_file(url, filename, show_status=True, desc=''):
    """ Downloads a file from the internet

    :param str url: URL to get file/data from
    :param str filename: File to save download to
    :param bool show_status: Show status with tqdm (Default is True)
    :param str desc: Description to show in status (Default is '')

    :return: Result of the download
    :rtype: bool

    """
    logger = logging.getLogger(__name__)
    r = requests.get(url, stream=True)

    try:
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

    except Exception as ex:
        logger.error(ex)
        return False
