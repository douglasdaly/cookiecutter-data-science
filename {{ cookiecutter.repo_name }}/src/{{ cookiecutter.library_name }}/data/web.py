# -*- coding: utf-8 -*-
"""
web.py

    Functions to facilitate data getting.

@author: Douglas Daly
@date: 11/17/2017
"""
#
#   Imports
#
import time
import requests
import urllib.request

from tqdm.auto import tqdm
from bs4 import BeautifulSoup

from .base import NoDataError


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
        URL to download the file from.
    filename: str
        File path to save the downloaded file to.

    show_status: bool, optional
        Whether or not to show a progress bar as the file is downloaded.
    desc: str, optional
        Description to display in the progress bar.

    Returns
    -------
    bool
        The result status of the download and save.

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


def get_data(url, retries=3, retry_wait=5):
    """Downloads data from the given URL

    Parameters
    ----------
    url: str
        URL to acquire the data from

    retries: int, optional
        Number of times to retry the request if it fails
    retry_wait: int, optional
        Number of seconds to wait between retries

    Raises
    ------
    MaxRetryError
        If the maximum number of retries is exceeded.

    Returns
    -------
    object
        The data requested from the given URL

    """
    if retries <= 0:
        raise MaxRetryError('Maximum retry count exceeded')

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
    except urllib.request.HTTPError:
        time.sleep(retry_wait)
        return get_data(url, retries-1)

    return data


def get_soup(url, parser='html.parser', **kwargs):
    """Gets a BeautifulSoup object of the web page specified

    Parameters
    ----------
    url: str
        URL to get web page data for.

    parser: str, optional
        HTML Parser to use.
    kwargs: optional
        Additional kwargs to pass to the get_data function.

    Raises
    ------
    NoDataError
        If no data is acquired from the specified URL.
    MaxRetryError
        If the maximum number of retries is exceeded.

    Returns
    -------
    BeautifulSoup
        Beautiful soup object of the page at the URL given.

    See Also
    --------
    get_data

    """
    html = get_data(url, **kwargs)

    soup = BeautifulSoup(html, parser)
    if soup is None:
        raise NoDataError("No data from URL")

    return soup


#
#   Exception Classes
#

class MaxRetryError(Exception):
    """
    Exception Class for Max retries
    """
    pass
