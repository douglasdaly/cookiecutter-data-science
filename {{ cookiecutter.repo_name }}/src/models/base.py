# -*- coding: utf-8 -*-
"""
Base model class

Implements the Model abstract class which is extended for specific
model implementations.

Also implements the ModelException, ParameterException and
HyperParameterException exceptions.

"""
#
#   Imports
#
from abc import ABCMeta, abstractmethod


#
#   Class Definitions
#

class Model(object, metaclass=ABCMeta):
    """
    Base Model Class

    Attributes
    ----------
    parameters : dict
        Dictionary of parameters for this model with their associated
        values.
    hyperparameters: dict
        Dictionary of hyper-parameters for training this model with
        their associated values.
    results: dict
        Dictionary of training results and their associated values.

    """

    def __init__(self):
        self._parameters = dict()
        self._hyper_parameters = dict()

        self._results = None

        self._opts_parameters = None
        self._opts_hyper_parameters = None
        self._opts_results = None

    # Properties

    @property
    def parameters(self):
        """ Parameters which are currently set for this model
        """
        return self._parameters

    @parameters.setter
    def parameters(self, params):
        """ Sets the parameters for this model

        Parameters
        ----------
        params: dict
            Full parameters dictionary to use

        Raises
        ------
        InvalidParameterException
            If one of the given parameters and/or value given is not
            valid.

        See Also
        --------
        parameters, add_parameter, remove_parameter

        """
        self._parameters.clear()
        for k, v in params.items():
            self.add_parameter(k, v)

    def add_parameter(self, param, value):
        """ Adds a single parameter to the parameter set

        :param str param: Parameter to add
        :param value: Value for the given parameter

        """
        if self._check_parameter(param, value)[0]:
            self._parameters[param] = value

    def remove_parameter(self, param):
        """ Removes the specified parameter from the model parameters

        :param str param: Name of the parameter to remove

        :return: Value of the parameter removed, None if param not in set

        """
        if param in self.parameters.keys():
            ret = self._parameters.pop(param)
        else:
            ret = None

        return ret

    def _check_parameter(self, param, value, suppress_exceptions=False):
        """ Checks if the given parameter and value combination are valid for this model

        :param str param: Parameter name
        :param value: Parameter value
        :param bool suppress_exceptions: Whether or not to ignore exceptions (Default is False)

        :return: If the given parameter and value combination are valid for this model
        :rtype: bool, str

        """
        except_type = None if suppress_exceptions \
            else InvalidParameterException
        return self.__param_check_helper(param, value, self._parameters,
                                         except_type)

    @property
    def hyper_parameters(self):
        """ Hyper-parameters which are currently set for this model
        """
        return self._hyper_parameters

    @hyper_parameters.setter
    def hyper_parameters(self, hyper_params):
        """ Sets the hyper-parameters for this model

        :param dict hyper_params: Hyper-parameter dictionary to set

        """
        self._hyper_parameters.clear()
        for k, v in hyper_params.items():
            self.add_hyper_parameter(k, v)

    def add_hyper_parameter(self, hyper_param, value):
        """ Adds a single hyper-parameter

        :param str hyper_param: Hyper-parameter to add
        :param value: Value for the given hyper-parameter

        """
        if self._check_hyper_parameter(hyper_param, value)[0]:
            self._hyper_parameters[hyper_param] = value

    def remove_hyper_parameter(self, hyper_param):
        """ Removes the specified hyper-parameter

        :param str hyper_param: Name of the hyper-parameter to remove

        :return: Value of the hyper-parameter removed, None if hyper_param not in set

        """
        if hyper_param in self.hyper_parameters.keys():
            ret = self._hyper_parameters.pop(hyper_param)
        else:
            ret = None

        return ret

    def _check_hyper_parameter(self, hyper_param, value, suppress_exceptions=False):
        """ Checks if the given hyper-parameter is valid

        :param str hyper_param: Hyper-Parameter name
        :param value: Hyper-Parameter value
        :param bool suppress_exceptions: Whether or not to ignore exceptions (Default is to False)

        :return: If the given hyper-parameter and value combination are valid for this model
        :rtype: bool, str

        """
        except_type = None if suppress_exceptions else InvalidHyperParameterException
        return self.__param_check_helper(hyper_param, value, self._opts_hyper_parameters, except_type)

    @staticmethod
    def __param_check_helper(param, value, option_dict, exception_type=None):
        """ Helper function for checking given Parameter and Value
        """
        if exception_type is not None:
            suppress_exceptions = False
        else:
            suppress_exceptions = True

        if param not in option_dict.keys():
            err_str = "No parameter named: " + param
            if not suppress_exceptions:
                raise exception_type(err_str)
            return False, err_str

        param_opt = option_dict[param]
        if not isinstance(value, param_opt.value_type):
            err_str = "Invalid type for " + param + ": found " + str(type(value)) + ", expected: " + \
                      str(param_opt.value_type)
            if not suppress_exceptions:
                raise exception_type(err_str)
            return False, err_str

        if param_opt.value_bounds is not None:
            if param_opt.value_bounds[0] is not None and value < param_opt.value_bounds[0]:
                err_str = "Invalid value given for " + param + ": Under min value of " + str(param_opt.value_bounds[0])
                if not suppress_exceptions:
                    raise exception_type(err_str)
                return False, err_str

            if param_opt.value_bounds[1] is not None and value > param_opt.value_bounds[1]:
                err_str = "Invalid value given for " + param + ": Over max value of " + str(param_opt.value_bounds[1])
                if not suppress_exceptions:
                    raise exception_type(err_str)
                return False, err_str

        return True, None

    def _check_init_parameters(self, use_defaults=True):
        """ Checks that required parameters are set

        :param bool use_defaults: Use default values for required parameters that aren't set

        :return: Whether or not the parameters in place are sufficient
        :rtype: bool

        """
        additional = self.__check_init_params_helper(self.parameters, self._opts_parameters, use_defaults)
        if additional is not None:
            for k, v in additional.items():
                self._parameters[k] = v
            return True
        else:
            return False

    def _check_init_hyper_parameters(self, use_defaults=True):
        """ Checks that required hyper-parameters are set

        :param bool use_defaults: Use default values for required hyper-parameters that aren't set

        :return: Whether or not the hyper-parameters in place are sufficient
        :rtype: bool

        """
        additional = self.__check_init_params_helper(self.hyper_parameters, self._opts_hyper_parameters, use_defaults)
        if additional is not None:
            for k, v in additional.items():
                self._hyper_parameters[k] = v
            return True
        else:
            return False

    @staticmethod
    def __check_init_params_helper(params, opt_params, use_defaults=True):
        """ Helper function for checking parameters

        :param dict params: Params to check
        :param dict opt_params: Params options dictionary to check against
        :param bool use_defaults: Use default values for required params that are unset

        :return: Additional params to add (None on error)
        :rtype: dict

        """
        dict_additional = dict()
        for k, v in opt_params.items():
            if v.value_required:
                if k not in params.keys():
                    if use_defaults and v.value_default is not None:
                        dict_additional[k] = v.value_default
                    else:
                        return None
        return dict_additional

    @property
    def results(self):
        """ Result metrics

        :return: Results dictionary
        :rtype: dict

        """
        return self._results

    # Save/Load Methods

    def save(self, tag):
        """ Saves this model

        :param str tag: Tag to use to save the model data

        :return: Success of the save
        :rtype: bool

        """
        raise NotImplementedError()

    def load(self, tag):
        """ Loads a model

        :param str tag: Tag to use to load the model data

        """
        raise NotImplementedError()

    # Abstract Methods

    @abstractmethod
    def construct(self, **kwargs):
        """ Constructs the model

        :param kwargs: Additional options for construction

        :return: Result of model construction
        :rtype: bool

        """
        pass

    @abstractmethod
    def run(self):
        """ Runs the primary training routine

        :return: Result of training run (success or failure)
        :rtype: bool

        """
        pass

    @abstractmethod
    def train(self, X, y, **kwargs):
        """ Trains the model on the given data

        :param X: Training data features
        :param y: Training data values/labels
        :param kwargs: Additional options for training

        :return: Result of the training operation (success or failure)
        :rtype: bool

        """
        pass

    @abstractmethod
    def predict(self, X, **kwargs):
        """ Predict outputs for the given features

        :param X: Features to predict outputs for
        :param kwargs: Additional options for prediction

        :return: Prediction y data on given X data
        :rtype: numpy.ndarray

        """
        pass

    # - Internal Classes

    class _ParameterOption(object):
        """
        Parameter Option internal class
        """

        def __init__(self, name, value_type, value_required=True, value_bounds=None, value_default=None):
            """ Default Constructor

            :param str name: Name of the Parameter these options are for
            :param type value_type: The type of value for this parameter
            :param bool value_required: Whether or not this is a required parameter (default is True)
            :param tuple value_bounds: [Optional] Bounds for this parameter (default is None)
            :param value_default: [Optional] Default value for this parameter (default is None)

            """
            self.name = name
            self.value_type = value_type
            self.value_required = value_required
            self.value_bounds = value_bounds
            self.value_default = value_default


#
#   Exception Classes
#

class ModelException(Exception):
    """
    Base Class for Model Exceptions
    """
    pass


class InvalidParameterException(ModelException):
    """
    Thrown when an Invalid Parameter is given
    """
    pass


class InvalidHyperParameterException(ModelException):
    """
    Thrown when an Invalid Hyper-Parameter is given
    """
    pass
