# -*- coding: utf-8 -*-
"""
Parameter factory functions
"""
#
#   Imports
#
from .base import ParameterMixin


#
#   Factory functions
#

def bound_mixin(name, checker):
    """Creates a new mixin class for bounded parameters

    Parameters
    ----------
    name : str
        Name of the property holding the bound's value.
    checker : callable
        Callable object/function to assess the boundary condition.

    Returns
    -------
    ParameterMixin
        New parameter mixin class for the bound specified.

    Raises
    ------
    ValueError
        If the given `checker` is not callable.

    """
    if not callable(checker):
        raise ValueError("The checker must be callable")
    cls_name = '%sBoundMixin' % name.replace(' ', '')
    prop_name = name.lower().replace(' ', '_')
    var_name = '_%s' % prop_name

    class _NewBoundMixin(ParameterMixin):

        def __init__(self, *args, **kwargs):
            setattr(self, var_name, kwargs.pop(prop_name, None))
            super(_NewBoundMixin, self).__init__(*args, **kwargs)

        def _check_helper(self, value, raise_exceptions=True) -> bool:
            ret = super(_NewBoundMixin, self)._check_helper(
                value, raise_exceptions=raise_exceptions
            )
            return ret and checker(value, getattr(self, var_name))

    @property
    def _w_property(self):
        return getattr(self, var_name)
    _w_property.func = prop_name

    @_w_property.setter
    def _w_property_setter(self, value):
        setattr(self, var_name, value)
    _w_property_setter.func = prop_name

    return type(cls_name, (_NewBoundMixin,), {prop_name: _w_property})
