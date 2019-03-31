# -*- coding: utf-8 -*-
"""
Parameter option classes for use in models.
"""
#
#   Imports
#
from .base import Parameter
from .mixins import MinMixin
from .mixins import MaxMixin


#
#   Parameter classes
#

class BoundedParameter(MinMixin, MaxMixin, Parameter):
    """
    Bounded parameter (min/max)
    """
    pass
