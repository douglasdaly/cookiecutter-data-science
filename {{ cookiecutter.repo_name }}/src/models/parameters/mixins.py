# -*- coding: utf-8 -*-
"""
Mixin classes for Parameters.
"""
#
#   Imports
#
from operator import gt, lt

from .factory import bound_mixin


#
#   Mixins
#

class MinMixin(bound_mixin('min', gt)):
    """
    Minimum value bound mixin class

    Attributes
    ----------
    min
        Maximum allowed value for this parameter.

    Parameters
    ----------
    min : optional
        Maximum allowed value for this parameter.

    """

    @min.setter
    def min(self, value):
        """Sets the minimum allowed value for this parameter

        Parameters
        ----------
        value
            Minimum allowed value for this parameter.

        Raises
        ------
        ValueError
            If the `value` given is not valid.

        """
        if hasattr(self, 'max') and value > self.max:
            raise ValueError("Minimum value cannot be greater than maximum"
                             " value")
        super(MinMixin, self).min = value


class MaxMixin(bound_mixin('max', lt)):
    """
    Minimum value bound mixin class

    Attributes
    ----------
    max
        Maximum allowed value for this parameter.

    Parameters
    ----------
    max : optional
        Maximum allowed value for this parameter.

    """

    @max.setter
    def max(self, value):
        """Sets the maximum allowed value for this parameter

        Parameters
        ----------
        value
            Maximum allowed value for this parameter

        Returns
        -------
        Value

        """
        if hasattr(self, 'min') and value < self.min:
            raise ValueError("Maximum value cannot be greater than minimum"
                             " value")
        super(MaxMixin, self).max = value
