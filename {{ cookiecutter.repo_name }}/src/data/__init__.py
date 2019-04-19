# -*- coding: utf-8 -*-
"""
A module containing helpful functions and classes acquiring and working with
data.
"""
from .exceptions import NoDataError
from . import web

__all__ = [
    # Exceptions
    'NoDataError',
    # Sub-modules
    'web',
]
